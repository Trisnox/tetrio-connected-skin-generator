#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import filedialog, ttk, colorchooser
from ext.gen import Skin_gen, ResolutionMismatch, MissingMino

def set_skin_location():
    dir = skin_location.get() if skin_location.get() else './'
    location = filedialog.askdirectory(initialdir = dir, title = "Select a folder")
    if location:
        skin_location.set(location)

def set_skin_export():
    location = filedialog.askdirectory(initialdir = './', title = "Select a folder")
    if location:
        skin_export.set(location)

def color_picker():
    color = colorchooser.askcolor(title='Color Picker')
    if any(color):
        disable_method.set(color[1])

def guess_method(location):
    s = ('s.png', 's.jpg', 's.jpeg')
    z = ('z.png', 'z.jpg', 'z.jpeg')
    l = ('l.png', 'l.jpg', 'l.jpeg')
    j = ('j.png', 'j.jpg', 'j.jpeg')
    t = ('t.png', 't.jpg', 't.jpeg')
    o = ('o.png', 'o.jpg', 'o.jpeg')
    i = ('i.png', 'i.jpg', 'i.jpeg')
    gb = ('gb.png', 'gb.jpg', 'gb.jpeg')
    gbd = ('gbd.png', 'gbd.jpg', 'gbd.jpeg')

    s1 = ('s1.png', 's1.jpg', 's1.jpeg')
    s2 = ('s2.png', 's2.jpg', 's2.jpeg')
    z1 = ('z1.png', 'z1.jpg', 'z1.jpeg')
    z2 = ('z2.png', 'z2.jpg', 'z2.jpeg')
    l1 = ('l1.png', 'l1.jpg', 'l1.jpeg')
    l2 = ('l2.png', 'l2.jpg', 'l2.jpeg')
    l3 = ('l3.png', 'l3.jpg', 'l3.jpeg')
    l4 = ('l4.png', 'l4.jpg', 'l4.jpeg')
    j1 = ('j1.png', 'j1.jpg', 'j1.jpeg')
    j2 = ('j2.png', 'j2.jpg', 'j2.jpeg')
    j3 = ('j3.png', 'j3.jpg', 'j3.jpeg')
    j4 = ('j4.png', 'j4.jpg', 'j4.jpeg')
    t1 = ('t1.png', 't1.jpg', 't1.jpeg')
    t2 = ('t2.png', 't2.jpg', 't2.jpeg')
    t3 = ('t3.png', 't3.jpg', 't3.jpeg')
    t4 = ('t4.png', 't4.jpg', 't4.jpeg')
    o1 = ('o1.png', 'o1.jpg', 'o1.jpeg')
    o2 = ('o2.png', 'o2.jpg', 'o2.jpeg')
    o3 = ('o3.png', 'o3.jpg', 'o3.jpeg')
    i1 = ('i1.png', 'i1.jpg', 'i1.jpeg')
    i2 = ('i2.png', 'i2.jpg', 'i2.jpeg')
    gb1 = ('gb1.png', 'gb1.jpg', 'gb1.jpeg')
    gb2 = ('gb2.png', 'gb2.jpg', 'gb2.jpeg')
    gb3 = ('gb3.png', 'gb3.jpg', 'gb3.jpeg')
    gbd1 = ('gbd1.png', 'gbd1.jpg', 'gbd1.jpeg')
    gbd2 = ('gbd2.png', 'gbd2.jpg', 'gbd2.jpeg')
    gbd3 = ('gbd3.png', 'gbd3.jpg', 'gbd3.jpeg')
    files = os.listdir(location)
    found1 = []
    found2 = []
    found3 = []
    found4 = []
    missing1 = []
    missing2 = []
    missing3 = []
    missing4 = []

    method_1 = (s, t, o, i)
    method_2 = (s, z, l, j, t, o, i, gb, gbd)
    method_3 = (s1, s2, t1, t2, t3, t4, o1, i1, i2)
    method_4 = (s1, s2, z1, z2, l1, l2, l3, l4, j1, j2, j3, j4, t1, t2, t3, t4, o1, o2, o3, i1, i2, gb1, gb2, gb3, gbd1, gbd2, gbd3)

    while True:
        for x, y, z in method_2:
            if x in files:
                found2.append(x)
            elif y in files:
                found2.append(y)
            elif z in files:
                found2.append(z)
            else:
                missing2.append(x)
                # break
                # faster but doesn't give info on what else is missing

        if not missing2:
            return 3, found2

        for x, y, z in method_1:
            if x in files:
                found1.append(x)
            elif y in files:
                found1.append(y)
            elif z in files:
                found1.append(z)
            else:
                missing1.append(x)
                # break
        
        if not missing1:
            return 2, found1
        
        for x, y, z in method_4:
            if x in files:
                found4.append(x)
            elif y in files:
                found4.append(y)
            elif z in files:
                found4.append(z)
            else:
                missing4.append(x)
                # break

        if not missing4:
            return 5, found4
        
        for x, y, z in method_3:
            if x in files:
                found3.append(x)
            elif y in files:
                found3.append(y)
            elif z in files:
                found3.append(z)
            else:
                missing3
        
        if not missing3:
            return 4, found3

        if len([*found1, *found2, *found3, *found4]) <= 0:
            raise MissingMino("Can't find a single file with correct name keys.", ())
        else:
            text = 'These files are missing for the following method:\n'
            if not len(missing1) == 4:
                text += "Universal:\n" + '\n'.join(missing1)
            if not len(missing2) == 9:
                text += "\n\nStandard:\n" + '\n'.join(missing2)
            if not len(missing3) == 27:
                text += "\n\nAdvanced:\n" + '\n'.join(missing3)

            raise MissingMino(text, ())

def generate_skin():
    for x in mainframe.winfo_children():
        try:
            x.config(state = tk.DISABLED)
        except:
            print('Unable to change to disable state for: ' + x.winfo_class())

    generate_button.config(text = 'Processing...')

    location = skin_location.get()
    if not location.endswith(os.sep):
        location += os.sep

    config = {
        'location': location,
        'automatic': False,
        'downscale': export_downscaled.get(),
        'disable': disable_method.get()
        }

    method = generation_method.get()
    if not method == 1:
        config['method'] = method
    else:
        try:
            method, files = guess_method(location)
        except MissingMino as e:
            minos = [x for x in e.missing]
            pop_up_revert_state('Unable to detect method: ' + e.message + '\n' + '\n'.join(minos))
            generate_button.config(text = 'Generate')
            return

        config['method'] = method
        config['automatic'] = files

    gen = Skin_gen(**config)

    try:
        skin = gen.start()
    except (ResolutionMismatch, MissingMino) as e:
        pop_up_revert_state(e.message)
        generate_button.config(text = 'Generate')
        return
    
    for name, img in skin.items():
        img.save(name)

    pop_up_revert_state('Skin successfully generated')
    generate_button.config(text = 'Generate')

def merge_skin():
    for x in mainframe.winfo_children():
        try:
            x.config(state = tk.DISABLED)
        except:
            print('Unable to change to disable state for: ' + x.winfo_class())

    merge_button.config(text = 'Processing...')

    location = skin_export.get()
    if not location.endswith(os.sep):
        location += os.sep

    config = {
        'location': location,
        'downscale': export_downscaled.get()
        }

    gen = Skin_gen(**config)
    try:
        skin = gen.merge_disabled_no_init()
    except MissingMino as e:
        pop_up_revert_state(e.message)
        merge_button.config(text = 'Merge')
        return
    
    for name, img in skin.items():
        img.save(name)

    pop_up_revert_state('Skin successfully merged')
    merge_button.config(text = 'Merge')

def pop_up_revert_state(text):
    for x in mainframe.winfo_children():
        try:
            x.config(state = tk.NORMAL)
        except:
            print('Unable to change to normal state for: ' + x.winfo_class())

    pop_up = tk.Toplevel(window)
    pop_up.title('Error')

    m = ttk.Frame(pop_up)
    m.grid(column = 0, row = 0, sticky = tk.N+tk.W+tk.E+tk.S)

    ttk.Label(m, text=text).grid(row = 1, column = 2)
    ttk.Label(m, text='').grid(row = 2, column = 2)
    ttk.Button(m, text = 'ok', command = lambda:pop_up.destroy()).grid(row = 3, column = 2)

    for x in m.winfo_children(): 
        x.grid_configure(padx=5, pady=5)

if __name__ == "__main__":
    window = tk.Tk()
    s = ttk.Style(window)

    s.configure('TFrame', background = '#0D1117')
    s.configure('TLabel', background = '#0D1117', foreground = '#E5E5E5')
    s.configure('TRadiobutton', background = '#0D1117', foreground = '#E5E5E5')
    s.configure('TEntry', background = '#0D1117', foreground = 'black')
    s.configure('TButton', background = '#0D1117')

    window.title('Tetr.io Connected Skin Generator')
    tk.Grid.columnconfigure(window, 0, weight = 1)
    tk.Grid.rowconfigure(window, 0, weight = 1)

    mainframe = ttk.Frame(window)
    mainframe.grid(column = 0, row = 0, sticky = tk.N+tk.W+tk.E+tk.S)

    for row_index in range(10):
        tk.Grid.rowconfigure(mainframe, row_index, weight = 1)
        for col_index in range(2):
            tk.Grid.columnconfigure(mainframe, col_index, weight = 1)

    skin_location_label = ttk.Label(mainframe, compound = tk.RIGHT, text = 'Skin location')
    skin_location_label.grid(row = 1, column = 1, sticky = tk.E)

    folders = [x for x in os.listdir('.') if os.path.isdir(x) and not x.startswith('.')]
    guess_folder = os.getcwd() + os.sep + folders[0] if len(folders) == 1 else None
    skin_location = tk.StringVar(value = guess_folder)

    skin_location_entry = ttk.Entry(mainframe, width = 50, textvariable = skin_location)
    skin_location_entry.grid(row = 1, column = 2, sticky = tk.W)

    browse_skin_button = ttk.Button(mainframe, text = 'Browse', width = 15, command = lambda:set_skin_location())
    browse_skin_button.grid(row = 1, column = 3, sticky = tk.W)


    skin_export_label = ttk.Label(mainframe, compound = tk.RIGHT, text = 'Export location')
    skin_export_label.grid(row = 2, column = 1, sticky = tk.E)

    skin_export = tk.StringVar(value = os.getcwd())

    skin_location_entry = ttk.Entry(mainframe, width = 50, textvariable = skin_export)
    skin_location_entry.grid(row = 2, column = 2, sticky = tk.W)

    browse_export_button = ttk.Button(mainframe, text = 'Browse', width = 15, command = lambda:set_skin_export())
    browse_export_button.grid(row = 2, column = 3, sticky = tk.W)


    ttk.Label(mainframe, text = '').grid(row = 3, column = 2)


    generation_method = tk.IntVar(value = 1)

    generation_method_label = ttk.Label(mainframe, text = 'Skin Generation Method')
    generation_method_label.grid(row = 4, column = 1)


    disable_method = tk.StringVar(value = "a")

    disable_method_label = ttk.Label(mainframe, text = 'Disabled Generation')
    disable_method_label.grid(row = 4, column = 2)


    export_downscaled = tk.IntVar(value = 1)

    export_downscaled_label = ttk.Label(mainframe, text = 'Export 1x (for >2x)')
    export_downscaled_label.grid(row = 4, column = 3)


    methods = {
        "Automatic": 1,
        "Universal": 2,
        "Standard": 3,
        "Mixed": 4,
        "Advanced": 5
    }

    future_row1 = 4
    for x, y in methods.items():
        future_row1 += 1
        ttk.Radiobutton(mainframe, text = x, value = y, variable = generation_method).grid(row = future_row1, column = 1)

    ttk.Radiobutton(mainframe, text = 'Chunk', value = 'a', variable = disable_method).grid(row = 5, column = 2)
    color_choice_button = ttk.Button(mainframe, text = "Flat Color", command = lambda:color_picker())
    color_choice_button.grid(row = 6, column = 2)

    ttk.Label(mainframe, text = '').grid(row = 10, column = 2)

    generate_button = ttk.Button(mainframe, text = 'Generate', command = lambda:generate_skin())
    generate_button.grid(row = 11, column = 1)


    merge_button = ttk.Button(mainframe, text = 'Merge', command = lambda:merge_skin())
    merge_button.grid(row = 11, column = 3)


    ttk.Radiobutton(mainframe, text = 'Yes', value = 1, variable = export_downscaled).grid(row = 5, column = 3)
    ttk.Radiobutton(mainframe, text = 'No', value = 0, variable = export_downscaled).grid(row = 6, column = 3)

    ttk.Label(mainframe, text = '').grid(row = 11, column = 2)


    ttk.Label(mainframe, text = 'version: 1.0.0', foreground = '#00FF00').grid(row = 13, column = 1, sticky=tk.W+tk.S)

    for x in mainframe.winfo_children(): 
        x.grid_configure(padx=5, pady=5)

    window.mainloop()
