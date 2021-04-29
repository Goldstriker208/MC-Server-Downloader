#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *

global paper_jar
global vanilla_jar
paper_jar = False
vanilla_jar = False

root = tk.Tk()
root.title("window")
# root.geometry("400x900")
root.geometry("400x400")


# MC Server Name Label
label_text = tk.StringVar()
label_text.set("Minecraft Server Name: ")

name_text = tk.StringVar()



label = tk.Label(root, textvar=label_text)
label.pack(fill='x', padx=5, pady=5)

name_entry = tk.Entry(root, textvar=name_text)
name_entry.pack(fill='x', padx=100, pady=5)





def paper():
    # Set to MC Paper Versions
    options = mc_paper_versions

    # Reset var and delete all old options
    menu.set('')
    drop['menu'].delete(0, 'end')

    # Insert list of new options (tk._setit hooks them up to var)
    new_choices = options
    for choice in new_choices:
        drop['menu'].add_command(label=choice, command=tk._setit(menu, choice))
        
    global paper_jar
    paper_jar = True
    res.configure(text = "Selected: Paper")
    print("Paper: " + str(paper_jar))


    

def vanilla():
    # Set to MC Paper Versions
    options = mc_vanilla_versions

    # Reset var and delete all old options
    menu.set('')
    drop['menu'].delete(0, 'end')

    # Insert list of new options (tk._setit hooks them up to var)
    new_choices = options
    for choice in new_choices:
        drop['menu'].add_command(label=choice, command=tk._setit(menu, choice))
        
    global vanilla_jar
    vanilla_jar = True
    res.configure(text = "Selected: Vanilla")
    print("Vanilla: " + str(vanilla_jar))

# MC Server label
label = ttk.Label(text="Choose your Minecraft Server")
label.pack(fill='x', padx=100, pady=5)

# Result Label
res = tk.Label(root)
res.pack()

# MC Server Buttons
paper_button = tk.Button(root, text="Paper", command=paper)
paper_button.pack(fill = 'x', padx=(150), pady=(5))


vanilla_button = tk.Button(root, text="Vanilla", command=vanilla)
vanilla_button.pack(fill= 'x', padx=(150), pady=(5))

# from dl_paper_jarNEW import mc_paper_versions

mc_paper_versions = [
    "Paper",
    "1.9",
    "1.10",
    "1.11",
    "1.12",
    "1.13",
    "1.14"
]

mc_vanilla_versions = [
    "Vanilla",
    "1.9",
    "1.10",
    "1.11",
    "1.12",
    "1.13",
    "1.14"
]
dropmenu = [""]
options = dropmenu
options2 = ["d"]

print("Paper: " + str(paper_jar))
print("Vanilla: " + str(vanilla_jar))


if paper_jar == True:
    print("trtue")
    options = mc_paper_versions

label2 = ttk.Label(text="Select MC Version")
label2.pack(fill='x', padx=100, pady=5)

# MC Version Label
menu= StringVar()
# menu.set(mc_paper_versions[-1])
menu.set("Select MC Version")


# MC Version Dropdown Menu
drop= OptionMenu(root, menu, *options)
drop.pack(fill='x', padx=100, pady=5)




# RAM Label
label2 = ttk.Label(text="RAM Allocation")
label2.pack(fill='x', padx=100, pady=5)

# RAM Text Entry
name_text2 = tk.StringVar()
name_entry2 = tk.Entry(root, textvar=name_text2)
name_entry2.pack(fill='x', padx=190, pady=5)

# EULA Checkbox
var1 = tk.IntVar()
c1 = tk.Checkbutton(root, text='Agree to EULA', variable=var1, onvalue=1, offvalue=0)
c1.pack()



def returnvalues():
    global mc_server_name
    global mc_version
    global ram
    global eula
    mc_server_name = name_entry.get()
    mc_version = menu.get()
    ram = name_entry2.get()
    eula = var1.get()
    print("MC Server Name: " + str(name_entry.get()))
    print("Paper: " + str(paper_jar))
    print("Vanilla: " + str(vanilla_jar))
    print("MC Version: " + str(menu.get()))
    print("Ram: " + str(name_entry2.get()))
    print("EULA: " + str(var1.get()))




    
# Button
next_button = tk.Button(root, text="Create MC Server", command=returnvalues)
next_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))




counter = 0


def do_job():
    global counter
    l.config(text='do {0}'.format(counter))
    counter += 1


l = tk.Label(root, text='', bg='yellow')
l.pack()

m = tk.Menu(root)
file_menu = tk.Menu(m, tearoff=0)
m.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=do_job)
file_menu.add_command(label='Open', command=do_job)
file_menu.add_command(label='Save', command=do_job)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

sub_menu = tk.Menu(file_menu)
file_menu.add_cascade(label='Import', menu=sub_menu, underline=0)
sub_menu.add_command(label='Submenu1', command=do_job)

# edit_menu = tk.Menu(m, tearoff=0)
# m.add_cascade(label='Edit', menu=edit_menu)
# edit_menu.add_command(label='Cut', command=do_job)
# edit_menu.add_command(label='Copy', command=do_job)
# edit_menu.add_command(label='Paste', command=do_job)


root.config(menu=m)
root.mainloop()

if paper_jar == True:
    mc_server = "Paper"
elif vanilla_jar == True:
    mc_server = "Vanilla"


print(mc_server_name)
print(mc_server)
print(mc_version)
print(ram)
print(eula)


