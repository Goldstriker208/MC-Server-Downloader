
import os
import time
import subprocess
import sys
import requests
import json
import os, sys, stat
from sys import platform
import time

def check_eula(eula):
    if eula != "agree":
        print("Did not agree to EULA")
        print("Exiting..")
        return False

    return True


# Fetch MC Paper Versions API JSON File
def fetch_verisons_json():   

    mc_paper_versions_url = 'https://api.papermc.io/v2/projects/paper/'

    # Filepath
    print("mc versions: " + mc_paper_versions_file_path)

    # Download Paper MC Versions JSON
    r = requests.get(mc_paper_versions_url, allow_redirects=True)
    print("Downloaded File: JSON " + mc_paper_versions_filename)

    # Save Paper MC Versions JSON to file path
    open(mc_paper_versions_file_path, 'wb').write(r.content)
    print("Saved JSON " + mc_paper_versions_filename + " to ", os.path.abspath(mc_paper_versions_file_path))
    with open(mc_paper_versions_file_path, 'r') as file:
        mc_paper_versions_data = file.read().replace('\n', '')

    readjson_paper_versions = json.loads(mc_paper_versions_data)["versions"]

    return readjson_paper_versions
    

def fetch_builds_json():

    paper_builds_url = f'https://api.papermc.io/v2/projects/paper/versions/{mc_version}'

    # Filepath
    print("paper builds: " + paper_builds_file_path)

    # Download Paper Builds JSON
    r = requests.get(paper_builds_url, allow_redirects=True)
    print("Downloaded File: JSON " + paper_builds_filename)

    # Save Paper Builds JSON to file path
    open(paper_builds_file_path, 'wb').write(r.content)
    print("Saved JSON " + paper_builds_filename + " to ", os.path.abspath(paper_builds_file_path))
    with open(paper_builds_file_path, 'r') as file:
        paper_builds_data = file.read().replace('\n', '')


    readjson_paper_builds = json.loads(paper_builds_data)["builds"]

    return readjson_paper_builds

def check_vaild_mc_version():

    for mc_paper_version in fetch_verisons_json():
        if mc_version == mc_paper_version:
            print("Vaild MC Paper Version")
            return True

    if mc_version != mc_paper_version: 
        return False


# Create MC Server Directory
def mc_server_dir(): 

    # Create Minecraft Server folder
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist
        print("Created Folder: " + dest_folder)

def download_jar():

    if check_vaild_mc_version() == True:

        # Download Latest Paper Build
        latest_build = fetch_builds_json()[-1]
        print("Downloading Latest Build: " + str(latest_build))
        jar_file = "paper-" + mc_version + "-" + str(latest_build) + ".jar"
        dl_paper_jar = "https://api.papermc.io/v2/projects/paper/versions/" + str(mc_version) + "/builds/" + str(latest_build) + "/downloads/" + jar_file
        r = requests.get(dl_paper_jar, allow_redirects=True)
        print("Downloaded: " + jar_file)
        open(dest_folder + "/" + jar_file, 'wb').write(r.content)
        print("Saved " + jar_file + " to", os.path.abspath(paper_builds_file_path))
        os.rename(dest_folder + "/" + jar_file, dest_folder + "/" + "paper.jar")

    else:
        print("Invaild MC Version")

def start_script():

    # Start Java
    # start_java = "java -Xms" + min_ram + "G -Xmx" + max_ram + "G -jar paper.jar nogui"
    start_java = f"java -Xms {min_ram}G -Xmx {max_ram}G -jar paper.jar nogui"

    # Creates batch script file
    myBat = open(f"{mc_server_name}/start.bat",'w+')
    myBat.write(start_java)
    myBat.close()

    # Creates shell script file
    myBat = open(f"{mc_server_name}/start.sh",'w+')
    myBat.write("#!/bin/sh\n")
    myBat.write('cd "$(dirname "$0")"\n')
    myBat.write("")
    myBat.write(start_java)
    myBat.close()
    #os.chmod(mc_server_name + "/start.sh", stat.S_IRWXO )

    st = os.stat(f"{mc_server_name}/start.sh")
    os.chmod(f"{mc_server_name}/start.sh", st.st_mode | stat.S_IEXEC)

    # Saves Minecraft Server Info
    file2write=open(f"{mc_server_name}/server-info.txt",'w')
    file2write.write("server-name = " + mc_server_name)
    file2write.write("\nmc-version = " + mc_version)
    file2write.write(f"\nmin-ram = {min_ram}")
    file2write.write(f"\nmax-ram = {max_ram}")
    file2write.close()

    # Set Eula
    file2write=open(dest_folder + "/" + "eula.txt",'w')
    file2write.write("eula=true")
    file2write.close()

    print("Open the batch script or shell script file to start your Minecraft Server")
    print(os.path.abspath(mc_server_name))

    time.sleep(1)
    os.system("cd " + (os.path.abspath(mc_server_name)))

    if platform == "linux":
        pass
    elif platform == "darwin":
        pass
    elif platform == "win32":
        subprocess.Popen("explorer /select," + (os.path.abspath(mc_server_name)))


# Ask user to agree to EULA
eula_input = str(input("Type agree if your agree to Mojangs EULA: ")).strip().lower()

if not check_eula(eula_input):
    time.sleep(2)
    sys.exit()

# mc_server_name = str(input("Minecraft Server Name: "))
mc_server_name = "mc-server"

# mc_version = str(input("Minecraft Version: "))
mc_version = "1.12.2"

# dest_folder = mc_server_name
dest_folder = "mc-server"

print("Type only the numbers of RAM(no GB at end)")
min_ram = str(input("Min Ram: "))
max_ram = str(input("Max Ram: "))

# File names
paper_builds_filename = "Paper Builds"
mc_paper_versions_filename = "MC Paper Versions"

#File paths
paper_builds_file_path = os.path.join(dest_folder, paper_builds_filename)
mc_paper_versions_file_path = os.path.join(dest_folder, mc_paper_versions_filename)

# Fetch JSON Files
fetch_verisons_json()
fetch_builds_json()

# Create MC Directory
mc_server_dir()

# Download paper jar file
download_jar()

# Create Start Script
start_script()


# Quit
sys.exit()