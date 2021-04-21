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


# Download Paper Jar file
def dl_jar(url: str, dest_folder: str, mc_version: str):

    # Create Minecraft Server folder
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist
        print("Created Folder: " + dest_folder)


    # Download Paper JSON file
    r = requests.get(url, stream=True)
    print("Downloaded File: JSON " + filename)   


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


from GUI import mc_version, server_name

# Convert lists to string
mc_version = ''.join(mc_version)
server_name = ''.join(server_name)

print(mc_version)

dest_folder = server_name

# Set defualt ram
min_ram = "2"
max_ram = "2"

# Variables and calls dl_jar function
json_url = 'https://papermc.io/api/v2/projects/paper/versions/' + mc_version
mc_paper_versions_json_url = 'https://papermc.io/api/v2/projects/paper/'
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

print("Open the batch file to start your Minecraft Server")
print(os.path.abspath(server_name))

time.sleep(1)
os.system("cd " + (os.path.abspath(server_name)))
subprocess.Popen("explorer /select," + (os.path.abspath(server_name)))



# Quit
sys.exit()