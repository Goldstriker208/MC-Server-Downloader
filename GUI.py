#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
import json
import os
import sys
import shutil
import subprocess
import time

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
    drop_down_mc_list = mc_paper_versions

    # Reset var and delete all old options
    drop_down_list.set('Select MC Paper Version')
    drop['menu'].delete(0, 'end')

    # Insert list of new options (tk._setit hooks them up to var)
    new_choices = drop_down_mc_list
    for choice in new_choices:
        drop['menu'].add_command(label=choice, command=tk._setit(drop_down_list, choice))
        
    global paper_jar
    paper_jar = True
    res.configure(text = "Selected: Paper")
    print("Paper: " + str(paper_jar))


    

def vanilla():
    # Set to MC Paper Versions
    drop_down_mc_list = mc_vanilla_versions

    # Reset var and delete all old options
    drop_down_list.set('Select MC Vanilla Version')
    drop['menu'].delete(0, 'end')

    # Insert list of new options (tk._setit hooks them up to var)
    new_choices = drop_down_mc_list
    for choice in new_choices:
        drop['menu'].add_command(label=choice, command=tk._setit(drop_down_list, choice))
        
    global vanilla_jar
    vanilla_jar = True
    res.configure(text = "Selected: Vanilla")
    print("Vanilla: " + str(vanilla_jar))

# MC Server label
label = tk.Label(text="Choose your Minecraft Server")
label.pack(fill='x', padx=100, pady=5)

# MC Server Result Label
res = tk.Label(root)
res.pack()

# MC Server Buttons
paper_button = tk.Button(root, text="Paper", command=paper)
paper_button.pack(fill = 'x', padx=(150), pady=(5))


vanilla_button = tk.Button(root, text="Vanilla", command=vanilla)
vanilla_button.pack(fill= 'x', padx=(150), pady=(5))

# from dl_paper_jarNEW import mc_paper_versions

# from dl_paper_json import mc_paper_versions

dest_folder = "jsons"

try:
    os.mkdir(dest_folder)
except FileExistsError:
    pass

try: 
    os.remove("jsons/MC Paper Versions") 
    # print("% s removed successfully" % path) 
except OSError as error: 
    pass
    # print(error) 
    # print("File path can not be removed") 



# Variables 

# JSON URL
mc_paper_versions_url = 'https://papermc.io/api/v2/projects/paper/'

# File name
mc_paper_versions_filename = "MC Paper Versions"

#File path
mc_paper_versions_file_path = os.path.join(dest_folder, mc_paper_versions_filename)





# Filepaths
print("mc versions: " + mc_paper_versions_file_path)


# Download Paper MC Versions JSON
r = requests.get(mc_paper_versions_url, allow_redirects=True)
print("Downloaded File: JSON " + mc_paper_versions_filename)

# Save Paper MC Versions JSON to file path
open(mc_paper_versions_file_path, 'wb').write(r.content)
print("Saved JSON " + mc_paper_versions_filename + " to ", os.path.abspath(mc_paper_versions_file_path))
with open(mc_paper_versions_file_path, 'r') as file:
    mc_paper_versions_data = file.read().replace('\n', '')


# Read JSON File
class readjson:
    def __init__(self, json_def):
        self.__dict__ = json.loads(json_def)

readjson_paper_versions = readjson(mc_paper_versions_data)

os.remove("jsons/MC Paper Versions")

# MC Paper Version List
global mc_paper_versions
mc_paper_versions = readjson_paper_versions.versions 


mc_vanilla_versions = [
    "",
]






if paper_jar == True:
    drop_down_mc_list = mc_paper_versions

label = tk.Label(text="Select MC Version")
label.pack(fill='x', padx=100, pady=5)

# Intialize MC Server Version Drop Down List
drop_down_list= StringVar()
drop_down_list.set("Select MC Server First")
# menu.set(mc_paper_versions[-1])
drop_down_list_item = [""]
drop_down_mc_list = drop_down_list_item





# MC Server Dropdown Menu
drop= OptionMenu(root, drop_down_list, *drop_down_mc_list)
drop.pack(fill='x', padx=100, pady=5)




# RAM Label
label = tk.Label(text="Dedicated RAM in GB's")
label.pack(fill='x', padx=100, pady=5)

# RAM Text Entry
ram_text = tk.StringVar()
ram_entry = tk.Entry(root, textvar=ram_text)
ram_entry.pack(fill='x', padx=190, pady=5)

# EULA Checkbox
eula_output = tk.IntVar()
eula_checkbox = tk.Checkbutton(root, text='Agree to EULA', variable=eula_output, onvalue=1, offvalue=0)
eula_checkbox.pack()



def returnvalues():
    global mc_server_name
    global mc_version
    global ram
    global eula
    mc_server_name = name_entry.get()
    mc_version = drop_down_list.get()
    ram = ram_entry.get()
    eula = eula_output.get()
    print("MC Server Name: " + str(name_entry.get()))
    print("Paper: " + str(paper_jar))
    print("Vanilla: " + str(vanilla_jar))
    print("MC Version: " + str(drop_down_list.get()))
    print("Ram: " + str(ram_entry.get()))
    print("EULA: " + str(eula_output.get()))
    root.quit()




    
# Button
next_button = tk.Button(root, text="Create MC Server", command=returnvalues)
next_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))




counter = 0


def do_job():
    global counter
    l.config(text='do {0}'.format(counter))
    counter += 1


# l = tk.Label(root, text='', bg='yellow')
# l.pack()

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


# print(mc_server_name)
# print(mc_server)
# print(mc_version)
# print(ram)
# print(eula)


