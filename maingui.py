import tkinter as tk
import tkinter.messagebox as msgbox
import sys 

# global file2write



list1 = []

class main_menu():
    def __init__(self, master):
        self.master = master
        # self.btn = tk.Button(master, text="Button", command=self.command)
        # self.btn.pack()
        self.label_text = tk.StringVar()
        self.label_text.set("Choose One")
        self.label = tk.Label(master, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)

        self.paper_button = tk.Button(master, text="Paper", command=self.open_paper_menu)
        self.paper_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))

        self.vanilla_button = tk.Button(master, text="Vanilla", command=self.open_vanilla_menu)
        self.vanilla_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))


    def open_paper_menu(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        # toplevel.geometry("350x350")
        app = paper_menu(toplevel)

    def open_vanilla_menu(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x350")
        app = vanilla_menu(toplevel)

class paper_menu:
    def __init__(self, master):
        self.master = master
        # self.frame = tk.Frame(self.master)
        # self.quitButton = tk.Button(self.frame, text = '1Quit', width = 25, command = self.command)
        # self.quitButton.pack()
        # self.frame.pack()

        self.label_text = tk.StringVar()
        self.label_text.set("Minecraft Server Name: ")

        self.name_text = tk.StringVar()

        
        self.label = tk.Label(master, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=10)

        self.label2 = tk.Label(master, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=0)

        self.name_entry = tk.Entry(master, textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        next_button = tk.Button(master, text="Next", command=self.server_name)
        next_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    # def command(self):
    #     self.master.withdraw()
    #     toplevel = tk.Toplevel(self.master)
    #     toplevel.geometry("350x350")
    #     app = Demo3(toplevel)

    def server_name(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        # toplevel.geometry("350x350")
        app = paper_menu2(toplevel)
        name = self.name_entry.get()
        file2write=open("server-info.txt",'w')
        file2write.write("server-name = " + name)
        file2write.close()
        list1.append(name)
        print(list1)
        print("Minecraft Server Name: " + name)
        # return name
        # from main import dest_folder
        # file2write=open("server-info.txt",'w')
        
        













class paper_menu2:
    def __init__(self, master):
        self.master = master
        # self.frame = tk.Frame(self.master)
        # self.quitButton = tk.Button(self.frame, text = '1Quit', width = 25, command = self.command)
        # self.quitButton.pack()
        # self.frame.pack()

        self.label_text = tk.StringVar()
        self.label_text.set("Minecraft Version: ")

        self.name_text = tk.StringVar()

        
        self.label = tk.Label(master, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=10)

        self.label2 = tk.Label(master, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=0)

        self.name_entry = tk.Entry(master, textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        next_button = tk.Button(master, text="Next", command=self.mc_version)
        next_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    # def command(self):
    #     self.master.withdraw()
    #     toplevel = tk.Toplevel(self.master)
    #     toplevel.geometry("350x350")
    #     app = Demo3(toplevel)

    def mc_version(self):
        self.master.withdraw()
        name = self.name_entry.get()
        file2write=open("server-info.txt",'w')
        file2write.write("\nmc-version = " + name)
        file2write.close()
        paper_menu2.eula(self)
        name = self.name_entry.get()
        list1.append(name)
        print(list1)
        print("Minecraft Version: " + name)
        # return name
       


    def eula(self):
        if msgbox.askyesno("Mojangs Eula", "Agree to Mojangs EULA?"):
            #yes
            print("Agreed to EULA")
            import maintogui
        else:
            #no
            message = "Window will close in 2 seconds - goodybye "
            self.after(2000, master.destroy)






class vanilla_menu:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = '2Quit', width = 25, command = self.command)
        self.quitButton.pack()
        self.frame.pack()
    def command(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x350")
        app = vanilla_menu(toplevel)




root = tk.Tk()
root.title("window")
# root.geometry("350x350")
cls = main_menu(root)
root.mainloop()


