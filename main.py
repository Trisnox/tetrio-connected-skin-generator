#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import filedialog, ttk, colorchooser
from ext.gen import Skin_gen, ResolutionMismatch, MissingMino

def set_skin_location():
    location = filedialog.askdirectory(initialdir = './', title = "Select a folder")
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
    files = os.listdir(location)
    found = []
    missing = []

    method_1 = (s, t, o, i)
    method_2 = (s, z, l, j, t, o, i, gb, gbd)
    # method 3 is very simple, just check on single file
    # we'll then handle the missing and optional at the skin checking

    while True:
        for x, y, z in method_2:
            if x in files:
                found.append(x)
            elif y in files:
                found.append(y)
            elif z in files:
                found.append(z)
            else:
                missing.append(x)

        if missing:
            missing = []
        else:
            return 3, found

        for x, y, z in method_1:
            if x in files:
                found.append(x)
            elif y in files:
                found.append(y)
            elif z in files:
                found.append(z)
            else:
                missing.append(x)
        
        if missing:
            if len(found) <= 0:
                raise MissingMino("Can't find a single file with correct name keys.", ())
            else:
                raise MissingMino('One or more mino are missing', missing)
        else:
            return 2, found

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
    
    # this won't be necessary anymore on v1.0.0
    if method == 4:
        pop_up_revert_state('Advanced method is not yet available.')
        generate_button.config(text = 'Generate')
        return

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
        "Advanced": 4
    }

    future_row1 = 4
    for x, y in methods.items():
        future_row1 += 1
        ttk.Radiobutton(mainframe, text = x, value = y, variable = generation_method).grid(row = future_row1, column = 1)

    ttk.Radiobutton(mainframe, text = 'Chunk', value = 'a', variable = disable_method).grid(row = 5, column = 2)
    color_choice_button = ttk.Button(mainframe, text = "Flat Color", command = lambda:color_picker())
    color_choice_button.grid(row = 6, column = 2)

    ttk.Label(mainframe, text = '').grid(row = 9, column = 2)


    generate_button = ttk.Button(mainframe, text = 'Generate', command = lambda:generate_skin())
    generate_button.grid(row = 10, column = 1)


    merge_button = ttk.Button(mainframe, text = 'Merge', command = lambda:merge_skin())
    merge_button.grid(row = 10, column = 3)


    ttk.Radiobutton(mainframe, text = 'Yes', value = 1, variable = export_downscaled).grid(row = 5, column = 3)
    ttk.Radiobutton(mainframe, text = 'No', value = 0, variable = export_downscaled).grid(row = 6, column = 3)

    ttk.Label(mainframe, text = '').grid(row = 11, column = 2)


    ttk.Label(mainframe, text = 'version: 0.2.0', foreground = '#00FF00').grid(row = 12, column = 1, sticky=tk.W+tk.S)

    for x in mainframe.winfo_children(): 
        x.grid_configure(padx=5, pady=5)

    window.mainloop()
