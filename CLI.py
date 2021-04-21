from dl_paper_jar import dl_jar
import os
import time
import subprocess
import sys


# Ask User Minecraft Server name, version, and min/max RAM
server_name = str(input("Minecraft Server Name: "))
mc_version = str(input("Minecraft Version: "))
dest_folder = server_name
min_ram = str(input("Min Ram: "))
max_ram = str(input("Max Ram: "))

# Variables and calls dl_jar function
json_url = 'https://papermc.io/api/v2/projects/paper/versions/' + mc_version
filename = json_url.split('/')[-1].replace(" ", "_")  # be careful with file names
file_path = os.path.join(dest_folder, filename)
dl_jar(json_url, dest_folder, mc_version)


# Creates batch file
start_java = "java -Xms" + min_ram + "G -Xmx" + max_ram + "G -jar paper.jar nogui"
myBat = open(server_name + "/" + "start.bat",'w+')
myBat.write(start_java)
myBat.close()



# Saves Minecraft Server Info
file2write=open(dest_folder + "/" + "server-info.txt",'w')
file2write.write("server-name = " + server_name)
file2write.write("\nmc-version = " + mc_version)
file2write.write("\nmin-ram = " + min_ram)
file2write.write("\nmax-ram = " + max_ram)
file2write.close()

# Ask user to agree to EULA
eula = str(input("Type agree if your agree to Mojangs EULA: "))
if eula == "agree":
    file2write=open(dest_folder + "/" + "eula.txt",'w')
    file2write.write("eula=true")
    file2write.close()
    
print("Open the batch file to start your Minecraft Server")
print(os.path.abspath(server_name))
time.sleep(1)
os.system("cd " + (os.path.abspath(server_name)))
subprocess.Popen("explorer /select," + (os.path.abspath(server_name)))

#Quit
sys.exit()