import requests
import json
import os
import sys
import shutil
import subprocess
import time

global filename
global file_path
global min_ram
global max_ram


def dl_jar(url: str, dest_folder: str, mc_version: str):

    # Create Minecraft Server folder
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist
        print("Created Folder: " + dest_folder)

    # filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    # file_path = os.path.join(dest_folder, filename)

    # Download Paper JSON file
    r = requests.get(url, stream=True)
    print("Downloaded File: JSON " + filename)   

    # # Save Paper JSON file to Minecraft Server folder
    # if r.ok:
    #     # print("Saved: " + filename + " to", os.path.abspath(file_path))
    #     with open(file_path, 'wb') as f:
    #         for chunk in r.iter_content(chunk_size=1024 * 8):
    #             if chunk:
    #                 f.write(chunk)
    #                 f.flush()
    #                 os.fsync(f.fileno())
    # else:  # HTTP status code 4XX/5XX
    #     print("Download failed: status code {}\n{}".format(r.status_code, r.text))



    # Save Paper JSON to file path
    r = requests.get(url, allow_redirects=True)
    open(file_path, 'wb').write(r.content)
    print("Saved JSON " + filename + "to ", os.path.abspath(file_path))
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', '')

    # Read Paper JSON 
    class readjson:
        def __init__(self, json_def):
            self.__dict__ = json.loads(json_def)
    readjson = readjson(data)
  
    # Download Latest Paper Build
    latest_build = readjson.builds[-1]
    print("Downloading Latest Build: " + str(latest_build))
    jar_file = "paper-" + mc_version + "-" + str(latest_build) + ".jar"
    dl_paper_jar = "https://papermc.io/api/v2/projects/paper/versions/" + str(mc_version) + "/builds/" + str(latest_build) + "/downloads/" + jar_file
    r = requests.get(dl_paper_jar, allow_redirects=True)
    print("Downloaded: " + jar_file)
    open(dest_folder + "/" + jar_file, 'wb').write(r.content)
    print("Saved " + jar_file + " to", os.path.abspath(file_path))
    os.rename(dest_folder + "/" + jar_file, dest_folder + "/" + "paper.jar")
    # original = 
    # target = 


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

# startserver = str(input("Would you like to start the Minecraft Server [Y/n] : "))

# if startserver == 'y':
#     pass

sys.exit()