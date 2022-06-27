import os
from PIL import Image
# GIF unsupported... yet, I hope you enjoy doing this frame by frame

# [x, y], this is size for automatic rotation
# divide it by 48, then multiply it for guessing cropping resolution
# by default 48 generate 1024x1024, 96 generate 2048, and so on. Though, beyond 2x won't likely necessary
# if you create bigger than 2x, you likely need to resize

# was planned to to checks through image size, but scraped anyways
# szljt_minimum_size = [48*3, 48*2]
# o_minimum_size = [48*2, 48*2]
# i_minimum_size = [48*3, 48*1]
# garbage_minimum_size = [48*3, 48*3]

# individual pieces matrix for advanced skin generation. Coming soon
s_r1 = None

class ResolutionMismatch(Exception):
    """
    Called when skin resolution doesn't match with the rest (mixing 1x with 2x)

    Eg: S piece is 144x96, meanwhile Z piece is 288x192 is invalid due to 1x skin mixed with 2x
        This also applies to other piece as well
    """
    def __init__(self, *args):
        self.f1 = args[0]
        self.f2 = args[1]
        self.f3 = args[2]
        self.message = f"Error: Checks fail\nThe first file (S mino) resolution is {self.f1}x, but '{self.f2}' resolution is {self.f3}x. All image must be a power of either 48 or 96 pixels instead of both."
        super(ResolutionMismatch, self).__init__(self.message)

class Skin_gen():
    def __init__(self, location):
        self.location = location
        self.images = []
        self.name_keys = []
        self.multiplication_size = None

    def close_images(self):
        try:
            for x in self.images:
                self.images.remove(x)
                x.close()
        except:
            pass

    # skin file checking
    def skin_check(self):
        s = ('s.png', 's.jpg', 's.jpeg')
        z = ('z.png', 'z.jpg', 'z.jpeg')
        l = ('l.png', 'l.jpg', 'l.jpeg')
        j = ('j.png', 'j.jpg', 'j.jpeg')
        t = ('t.png', 't.jpg', 't.jpeg')
        o = ('o.png', 'o.jpg', 'o.jpeg')
        i = ('i.png', 'i.jpg', 'i.jpeg')
        gb = ('gb.png', 'gb.jpg', 'gb.jpeg')
        gbd = ('gbd.png', 'gbd.jpg', 'gbd.jpeg')
        missing = []
        found = [] # can't find file if format is not supplied, fortunately it's case insensitive
        files = os.listdir(self.location)

        for x, y, z in (s, z, l, j, t, o, i, gb, gbd):
            if x in files:
                found.append(x)
            elif y in files:
                found.append(y)
            elif z in files:
                found.append(z)
            else:
                missing.append(x)

        self.name_keys = found
        return missing, found
    
    # skin multiplication resolution checking
    def open_images(self):
        def check(fn, w, h):
            if fn.lower().startswith(('s', 'z', 'l', 'j', 't', 'o')):
                if not h/2/48 == self.multiplication_size:
                    return False, fn, int(h/2/48)
            elif fn.lower().startswith('i'):
                if not h/48 == self.multiplication_size:
                    return False, fn, int(h/48)
            elif fn.lower().startswith('gb'):
                if not h/3/48 == self.multiplication_size:
                    return False, fn, int(h/3/48)
            return True, None, None

        mismatch = []
        for x in self.name_keys:
            file_name = x
            x = self.location + x
            i = Image.open(x)
            self.images.append(i)

            w, h = i.size
            if not self.multiplication_size:
                self.multiplication_size = int(h/2/48)
                continue
            
            a, b, c = check(file_name, w, h)
            if not a:
                mismatch.append((b, c))
        
        if mismatch:
            self.close_images()
            raise ResolutionMismatch((str(int(self.multiplication_size))), (', '.join([x[0] for x in mismatch])), ('x, '.join([str(x[1]) for x in mismatch])))

        return


    def generate_skin(self):
        if not self.images:
            self.open_images()
        
        # minos are always appeared on these order, szljtoi and gb gbd
        minos = []
        m = self.multiplication_size # shorthand
        s = 48 * m

        ############
        # 01 02 03 #
        # 04 05 06 #
        # 07 08 09 #
        ############
        # because pil crop is so stupid that made me headache
        # fits for any pieces
        crop_matrix = {
            1: (0, 0, s, s), 2: (s, 0, s*2, s), 3: (s*2, 0, s*3, s),
            4: (0, s, s, s*2), 5: (s, s, s*2, s*2), 6: (s*2, s, s*3, s*2),
            7: (0, s*2, s, s*3), 8: (s, s*2, s*2, s*3), 9: (s*2, s*2, s*3, s*3)
            }

        ###############
        # 01 11 20 14 #
        # 02 21 22 23 #
        # 03 12 24 13 #
        # 19 04 05 06 #
        # 07 10 15 18 #
        # 08 09 16 17 #
        ###############
        # this is differ for cropping, garbage also compatible
        matrix = {
            1: (0, 0), 2: (0, 48*m), 3: (0, 96*m),
            4: (48*m, 144*m), 5: (96*m, 144*m), 6: (144*m, 144*m),
            7: (0, 192*m), 8: (0, 240*m), 9: (48*m, 240*m), 10: (48*m, 192*m),
            11: (48*m, 0), 12: (48*m, 96*m), 13: (144*m, 96*m), 14: (144*m, 0),
            15: (96*m, 192*m), 16: (96*m, 240*m), 17: (144*m, 240*m), 18: (144*m, 192*m),
            19: (0, 144*m),
            20: (96*m, 0), 21:(48*m, 48*m), 22: (96*m, 48*m), 23: (144*m, 48*m), 24: (96*m, 96*m) 
            }

        for x, img in enumerate(self.images):
            if x >= 7:
                canvas = Image.new('RGBA', (192*m, 192*m))
            else:
                canvas = Image.new('RGBA', (192*m, 288*m))

            if x == 0: # s
                block_1 = img.crop(crop_matrix[2])
                block_2 = img.crop(crop_matrix[3])
                block_3 = img.crop(crop_matrix[4])
                block_4 = img.crop(crop_matrix[5])

                canvas.paste(block_1, matrix[7])
                canvas.paste(block_2, matrix[6])
                canvas.paste(block_3, matrix[4])
                canvas.paste(block_4, matrix[9])

                # automatic rotation, the catch? piece is trivial in each rotation
                # non trivial ones are like puyo puyo/four.lol/default connected on tetr.io/res and etc
                canvas.paste(block_1.rotate(90), matrix[8])
                canvas.paste(block_4.rotate(90), matrix[10])
                canvas.paste(block_2.rotate(90), matrix[1])
                canvas.paste(block_3.rotate(90), matrix[3])

                # beyond canvas.paste is basically generate everything else that were necessary
                # through splicing image, of course the result won't be much satisfying for non trivial ones
                singular = Image.new('RGBA', (48*m, 48*m))

                singular.paste(block_3.crop((0, 0, int(s/2), s)), (0, 0))
                singular.paste(block_2.crop((int(s/2), 0, s, s)), (int(s/2), 0))

                canvas.paste(singular, matrix[19])

                minos.append(canvas)

            elif x == 1: # z
                block_1 = img.crop(crop_matrix[1])
                block_2 = img.crop(crop_matrix[2])
                block_3 = img.crop(crop_matrix[5])
                block_4 = img.crop(crop_matrix[6])
                
                canvas.paste(block_1, matrix[4])
                canvas.paste(block_2, matrix[10])
                canvas.paste(block_3, matrix[8])
                canvas.paste(block_4, matrix[6])

                canvas.paste(block_3.rotate(90), matrix[9])
                canvas.paste(block_2.rotate(90), matrix[7])
                canvas.paste(block_4.rotate(90), matrix[1])
                canvas.paste(block_1.rotate(90), matrix[3])

                singular = Image.new('RGBA', (48*m, 48*m))

                singular.paste(block_1.crop((0, 0, int(s/2), s)), (0, 0))
                singular.paste(block_4.crop((int(s/2), 0, s, s)), (int(s/2), 0))

                canvas.paste(singular, matrix[19])

                minos.append(canvas)

            elif x == 2: # l
                block_1 = img.crop(crop_matrix[3])
                block_2 = img.crop(crop_matrix[4])
                block_3 = img.crop(crop_matrix[5])
                block_4 = img.crop(crop_matrix[6])
                
                canvas.paste(block_1, matrix[1])
                canvas.paste(block_2, matrix[4])
                canvas.paste(block_3, matrix[5])
                canvas.paste(block_4, matrix[9])

                canvas.paste(block_1.rotate(-90), matrix[6])
                canvas.paste(block_2.rotate(90), matrix[3])
                canvas.paste(block_3.rotate(-90), matrix[2])

                canvas.paste(block_4.rotate(90), matrix[10])
                canvas.paste(block_4.rotate(90*2), matrix[7])
                canvas.paste(block_4.rotate(90*3), matrix[8])

                singular = Image.new('RGBA', (48*m, 48*m))

                singular.paste(block_2.crop((0, 0, int(s/2), s)), (0, 0))
                singular.paste(block_1.rotate(-90).crop((int(s/2), 0, s, s)), (int(s/2), 0))

                canvas.paste(singular, matrix[19])

                minos.append(canvas)

            elif x == 3: # j
                block_1 = img.crop(crop_matrix[1])
                block_2 = img.crop(crop_matrix[4])
                block_3 = img.crop(crop_matrix[5])
                block_4 = img.crop(crop_matrix[6])
                
                canvas.paste(block_1, matrix[1])
                canvas.paste(block_2, matrix[8])
                canvas.paste(block_3, matrix[5])
                canvas.paste(block_4, matrix[6])

                canvas.paste(block_1.rotate(90), matrix[4])
                canvas.paste(block_3.rotate(90), matrix[2])
                canvas.paste(block_4.rotate(-90), matrix[3])
                
                canvas.paste(block_2.rotate(90), matrix[9])
                canvas.paste(block_2.rotate(90*2), matrix[10])
                canvas.paste(block_2.rotate(90*3), matrix[7])

                singular = Image.new('RGBA', (48*m, 48*m))

                singular.paste(block_4.crop((int(s/2), 0, s, s)), (int(s/2), 0))
                singular.paste(block_1.rotate(90).crop((0, 0, int(s/2), s)), (0, 0))

                canvas.paste(singular, matrix[19])

                minos.append(canvas)

            elif x == 4: # t
                block_1 = img.crop(crop_matrix[2])
                block_2 = img.crop(crop_matrix[4])
                block_3 = img.crop(crop_matrix[5])
                block_4 = img.crop(crop_matrix[6])
                
                canvas.paste(block_1, matrix[1])
                canvas.paste(block_2, matrix[4])
                canvas.paste(block_3, matrix[15])
                canvas.paste(block_4, matrix[6])

                canvas.paste(block_2.rotate(90), matrix[3])

                canvas.paste(block_3.rotate(90), matrix[17])
                canvas.paste(block_3.rotate(90*2), matrix[16])
                canvas.paste(block_3.rotate(90*3), matrix[18])

                singular = Image.new('RGBA', (48*m, 48*m))

                singular.paste(block_2.crop((0, 0, int(s/2), s)), (0, 0))
                singular.paste(block_4.crop((int(s/2), 0, s, s)), (int(s/2), 0))

                canvas.paste(singular, matrix[19])

                straight_mino = Image.new('RGBA', (48*m, 48*m))

                straight_mino.paste(block_4.crop((0, 0, int(s/2), s)), (0,0))
                straight_mino.paste(block_2.crop((int(s/2), 0, s, s)), (int(s/2),0))

                canvas.paste(straight_mino, matrix[5])
                canvas.paste(straight_mino.rotate(90), matrix[2])

                corner_turn = Image.new('RGBA', (96*m, 96*m))

                corner = Image.new('RGBA', (48*m, 48*m))

                corner.paste(block_1.crop((0, 0, int(s/2), int(s/2))), (0, 0))
                corner.paste(block_2.crop((int(s/2), 0, s, int(s/2))), (int(s/2), 0))
                corner.paste(block_1.crop((0, int(s/2), int(s/2), s)), (0, int(s/2)))

                corner_turn.paste(block_3, matrix[2])
                corner_turn.paste(block_3, matrix[21])
                corner_turn.paste(block_3.rotate(180), matrix[1])
                corner_turn.paste(block_3.rotate(180), matrix[11])
                
                canvas.paste(corner_turn, matrix[7])

                canvas.paste(corner, matrix[7], corner)
                canvas.paste(corner.rotate(90), matrix[8], corner.rotate(90))
                canvas.paste(corner.rotate(90*2), matrix[9], corner.rotate(90*2))
                canvas.paste(corner.rotate(90*3), matrix[10], corner.rotate(90*3))

                minos.append(canvas)

            elif x == 5: # o
                block_1 = img.crop(crop_matrix[1])
                block_2 = img.crop(crop_matrix[4])
                block_3 = img.crop(crop_matrix[5])
                block_4 = img.crop(crop_matrix[2])
                
                canvas.paste(block_1, matrix[11])
                canvas.paste(block_2, matrix[12])
                canvas.paste(block_3, matrix[13])
                canvas.paste(block_4, matrix[14])

                singular = Image.new('RGBA', (48*m, 48*m))

                singular.paste(block_1.crop((0, 0, int(s/2), int(s/2))), (0, 0))
                singular.paste(block_4.crop((int(s/2), 0, s, int(s/2))), (int(s/2), 0))
                singular.paste(block_2.crop((0, int(s/2), int(s/2), s)), (0, int(s/2)))
                singular.paste(block_3.crop((int(s/2), int(s/2), s, s)), (int(s/2), int(s/2)))

                ending_cap = Image.new('RGBA', (48*m, 48*m))

                ending_cap.paste(block_1.crop((0, 0, int(s/2), s)), (0, 0))
                ending_cap.paste(block_4.crop((int(s/2), 0, s, s)), (int(s/2), 0))

                canvas.paste(ending_cap, matrix[1])
                canvas.paste(ending_cap.rotate(180), matrix[3])
                canvas.paste(ending_cap.rotate(-90), matrix[6])
                canvas.paste(ending_cap.rotate(90), matrix[4])

                canvas.paste(singular, matrix[19])

                minos.append(canvas)

            elif x == 6: # i
                block_1 = img.crop(crop_matrix[1])
                block_2 = img.crop(crop_matrix[2])
                block_3 = img.crop(crop_matrix[3])
                
                canvas.paste(block_1, matrix[4])
                canvas.paste(block_2, matrix[5])
                canvas.paste(block_3, matrix[6])

                canvas.paste(block_1.rotate(90), matrix[3])
                canvas.paste(block_2.rotate(90), matrix[2])
                canvas.paste(block_3.rotate(90), matrix[1])

                singular = Image.new('RGBA', (48*m, 48*m))

                singular.paste(block_1.crop((0, 0, int(s/2), s)), (0, 0))
                singular.paste(block_3.crop((int(s/2), 0, s, s)), (int(s/2), 0))

                canvas.paste(singular, matrix[19])

                minos.append(canvas)

            elif x == 7 or x == 8: # gb
                block_1 = img.crop(crop_matrix[1])
                block_2 = img.crop(crop_matrix[2])
                block_3 = img.crop(crop_matrix[3])
                block_4 = img.crop(crop_matrix[4])
                block_5 = img.crop(crop_matrix[5])
                block_6 = img.crop(crop_matrix[6])
                block_7 = img.crop(crop_matrix[7])
                block_8 = img.crop(crop_matrix[8])
                block_9 = img.crop(crop_matrix[9])
                
                canvas.paste(block_1, matrix[11])
                canvas.paste(block_2, matrix[20])
                canvas.paste(block_3, matrix[14])
                canvas.paste(block_4, matrix[21])
                canvas.paste(block_5, matrix[22])
                canvas.paste(block_6, matrix[23])
                canvas.paste(block_7, matrix[12])
                canvas.paste(block_8, matrix[24])
                canvas.paste(block_9, matrix[13])

                bar = Image.new('RGBA', (144*m, 48*m))

                bar.paste(block_1.crop((0, 0, s, int(s/2))), matrix[1])
                bar.paste(block_2.crop((0, 0, s, int(s/2))), matrix[11])
                bar.paste(block_3.crop((0, 0, s, int(s/2))), matrix[20])
                bar.paste(block_7.crop((0, int(s/2), s, s)), (0, int(s/2)))
                bar.paste(block_8.crop((0, int(s/2), s, s)), (48*m, int(s/2)))
                bar.paste(block_9.crop((0, int(s/2), s, s)), (96*m, int(s/2)))

                bar_vert = bar.rotate(90, expand=True)
                canvas.paste(bar, matrix[4])
                canvas.paste(bar_vert, matrix[1])

                singular = Image.new('RGBA', (48*m, 48*m))

                singular.paste(block_1.crop((0, 0, int(s/2), int(s/2))), (0, 0))
                singular.paste(block_3.crop((int(s/2), 0, s, int(s/2))), (int(s/2), 0))
                singular.paste(block_7.crop((0, int(s/2), int(s/2), s)), (0, int(s/2)))
                singular.paste(block_9.crop((int(s/2), int(s/2), s, s)), (int(s/2), int(s/2)))

                canvas.paste(singular, matrix[19])

                minos.append(canvas)

        return minos, self.multiplication_size
                
    def combine_images(self, minos):
        offset_x = 192 * self.multiplication_size
        offset_y = 288 * self.multiplication_size

        canvas = Image.new('RGBA', (1024 * self.multiplication_size, 1024 * self.multiplication_size))
        for x, img in enumerate(minos):
            if x == 0: # s
                canvas.paste(img, (offset_x * 3, 0))
            elif x == 1: # z
                canvas.paste(img, (0, 0))
            elif x == 2: # l
                canvas.paste(img, (offset_x, 0))
            elif x == 3: # j
                canvas.paste(img, (offset_x, offset_y))
            elif x == 4: # t
                canvas.paste(img, (offset_x * 2, offset_y))
            elif x == 5: # o
                canvas.paste(img, (offset_x * 2, 0))
            elif x == 6: # i
                canvas.paste(img, (0, offset_y))
            elif x == 7: # gb
                canvas.paste(img, (offset_x * 4, 0))
            else: #gdb
                canvas.paste(img, (offset_x * 4, offset_x))
        
        return canvas

    def fill_gray(self, skin, percent):
        offset_x = 192 * self.multiplication_size
        offset_y = 288 * self.multiplication_size

        skin.paste((int(255*percent/100), int(255*percent/100), int(255*percent/100)), (offset_x * 3, offset_y, offset_x * 4, offset_y * 2))

        return skin

    def generate_disabled(self, minos): #s, z, l, j, t, o, i, gb, gbd
        s = minos[0]
        t = minos[4]
        o = minos[5]
        i = minos[6]
        m = self.multiplication_size
        canvas = Image.new('RGBA', (192 * m, 288 * m))
        canvas.paste(i.crop((0, 0, 288 * m, 192 * m)), (0, 0))
        canvas.paste(o.crop((48 * m, 0, 288 * m, 144 * m)), (48 * m, 0))
        canvas.paste(s.crop((0, 192 * m, 96 * m, 288 * m)), (0, 192*m))
        canvas.paste(t.crop((96 * m, 192 * m, 192 * m, 288 * m)), (96 * m, 192 * m))

        return canvas

# check if result and disabled is exist
if os.path.isfile('./result.png') and os.path.isfile('./disabled.png'):
    user_input = input('Result image and disabled mino is found, would you like to merge them? [Y/N]: ').lower()

    if user_input == 'y':
        check_1x = os.path.isfile('./result_1x.png')
        with Image.open('./disabled.png') as d:
            with Image.open('./result.png') as r:
                w, h = d.size
                m = int(w/96/2)
                r.paste(d, (192 * m * 3, 288 * m))
                r.save('result.png')
                if check_1x:
                    w, h = r.size
                    r.resize((int(w/m), int(h/m)), Image.Resampling(1)).save('result_1x.png')

        print('\nSuccessfully merged.')
        exit()

elif os.path.isfile('./result.png'):
    print("'result.png' is detected inside directory, this will overwrite current file\n")

location = None
current_folder = os.getcwd()
instant = False

# small QOL
# check if skin folder is on current script directory, if there many, ask user by choosing index, otherwise ask user to supply
folders = [x for x in os.listdir('.') if os.path.isdir(x) and not x.startswith('.')]
if len(folders) == 1:
    location = folders[0]
    instant = True

elif len(folders) >= 1:
    print('\n')
    for x, y in enumerate(folders):
        print(str((x+1)) + ". " + y)
    index_input = input("\nMultiple folder found inside directory, type index number to choose folder, otherwise type anything else: ")
    try:
        index = int(index_input) - 1
        if index < 0:
            raise IndexError
        location = current_folder + "\\" + folders[int(index_input) - 1]
    except (ValueError, IndexError):
        location = None

while True:
    if not location:
        location = input("copy & paste/drag & drop the root folder location of your skin here: ")

    location = location.strip('\"\'')

    if not location.endswith('\\'):
        location += "\\"

    print('\n')

    gen = Skin_gen(location = location)

    missing_skin, skin_file = gen.skin_check()

    if missing_skin and instant:
        instant = False
        location = None
        continue

    elif missing_skin:
        print('These minos are missing inside your skin folder (supported formats: png, jpg):\n' + '\n'.join(missing_skin))
        exit()
    
    break

connected_minos, multiplication_size = gen.generate_skin()

connected_skin = gen.combine_images(connected_minos)

user_input = input('Skin successfully generated. Would you like to generate flat color for disabled? If not, a disabled mino will generated for you to edit [Y/N]: ').lower()
if user_input == "y":
    color = input("\nInput a number between 0-100. 0 is black, 100 is white: ")
    while True:
        try:
            color = int(color)
            if color > 100 or color < 0:
                raise Exception
            break
        except:
            color = input("\nInvalid number, try again: ")
    connected_skin = gen.fill_gray(connected_skin, color)
else:
    disabled = gen.generate_disabled(connected_minos)
    disabled.save('disabled.png')
    print("\nDisabled mino successfully saved as 'disabled.png'. Once you done edit the skin, run this script again to merge them.")

connected_skin.save('result.png')
if multiplication_size > 1:
    user_input = input(("\nSkin successfully saved as 'result.png'.\n\nSince you were exporting 2x skin, would you like to also export 1x skin too? [Y/N]: ")).lower()
    if user_input == 'y':
        w, h = connected_skin.size

        # I know nearest is best resample for most situation, but lanczos also seems doing a great job for both non pixel and pixelized skins
        downscaled = connected_skin.resize((int(w/multiplication_size), int(h/multiplication_size)), Image.Resampling(1))
        downscaled.save('result_1x.png')
        print("\nSkin successfully saved as 'result_1x.png'")
else:
    print("\nSkin successfully saved as 'result.png'")
