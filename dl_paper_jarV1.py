import requests
import json
import os
import sys
import stat
import shutil
import subprocess
from sys import platform
import time

# Global variables
global paper_builds_filename
global paper_builds_file_path
global mc_paper_versions_filename
global mc_paper_versions_file_path
global min_ram
global max_ram

# Function to download Paper Jar file
def dl_jar(paper_builds_url: str, mc_paper_versions_url: str, dest_folder: str, mc_version: str):
    # Create Minecraft Server folder
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist
        print("Created Folder: " + dest_folder)

    # Download Paper Builds JSON
    r = requests.get(paper_builds_url, allow_redirects=True)
    print("Downloaded File: JSON " + paper_builds_filename)

    # Save Paper Builds JSON to file path
    open(paper_builds_file_path, 'wb').write(r.content)
    print("Saved JSON " + paper_builds_filename + " to ", os.path.abspath(paper_builds_file_path))
    with open(paper_builds_file_path, 'r') as file:
        paper_builds_data = file.read().replace('\n', '')

    # Filepaths
    print("mc versions: " + mc_paper_versions_file_path)
    print("paper builds: " + paper_builds_file_path)

    # Download Paper MC Versions JSON
    r = requests.get(mc_paper_versions_url, allow_redirects=True)
    print("Downloaded File: JSON " + mc_paper_versions_filename)

    # Save Paper MC Versions JSON to file path
    open(mc_paper_versions_file_path, 'wb').write(r.content)
    print("Saved JSON " + mc_paper_versions_filename + " to ", os.path.abspath(mc_paper_versions_file_path))
    with open(mc_paper_versions_file_path, 'r') as file:
        mc_paper_versions_data = file.read().replace('\n', '')

    # Read JSON Files
    class readjson:
        def __init__(self, json_def):
            self.__dict__ = json.loads(json_def)

    readjson_paper_builds = readjson(paper_builds_data)
    readjson_paper_versions = readjson(mc_paper_versions_data)

    global mc_paper_versions
    mc_paper_versions = readjson_paper_versions.versions + readjson_paper_versions.version_groups

    # Return mc_paper_versions and readjson_paper_builds
    return mc_paper_versions, readjson_paper_builds



# Function to download the latest Paper build
def download_latest_paper_build(mc_version, dest_folder, paper_builds_file_path):
    # Get the latest build number
    latest_build = readjson_paper_builds.builds[-1]
    print("Downloading Latest Build: " + str(latest_build))
    jar_file = "paper-" + mc_version + "-" + str(latest_build) + ".jar"
    dl_paper_jar = f"https://papermc.io/api/v2/projects/paper/versions/{mc_version}/builds/{latest_build}/downloads/{jar_file}"
    r = requests.get(dl_paper_jar, allow_redirects=True)
    print("Downloaded: " + jar_file)

    # Save the JAR file
    jar_path = os.path.join(dest_folder, jar_file)
    open(jar_path, 'wb').write(r.content)
    print("Saved " + jar_file + " to", os.path.abspath(jar_path))

    # Rename to "paper.jar"
    os.rename(jar_path, os.path.join(dest_folder, "paper.jar"))

# Function to check valid MC version
def check_valid_mc_version(mc_version, mc_paper_versions):
    for mc_paper_version in mc_paper_versions:
        if mc_version == mc_paper_version:
            print("Valid MC Paper Version")
            return True
    return False

# Main execution
try:
    from GUI import mc_server_name, mc_server, mc_version, ram, eula
except ImportError and OSError as error:
    sys.exit()

# Convert eula to boolean
eula = eula == 1

dest_folder = mc_server_name
min_ram = ram
max_ram = ram

paper_builds_url = 'https://papermc.io/api/v2/projects/paper/versions/' + mc_version
mc_paper_versions_url = 'https://papermc.io/api/v2/projects/paper/'
paper_builds_filename = "Paper Builds"
mc_paper_versions_filename = "MC Paper Versions"
paper_builds_file_path = os.path.join(dest_folder, paper_builds_filename)
mc_paper_versions_file_path = os.path.join(dest_folder, mc_paper_versions_filename)

# Call dl_jar and get mc_paper_versions and readjson_paper_builds
mc_paper_versions, readjson_paper_builds = dl_jar(paper_builds_url, mc_paper_versions_url, dest_folder, mc_version)

# Check valid MC version using mc_paper_versions
if not check_valid_mc_version(mc_version, mc_paper_versions):
    print("Invalid MC Version")
    sys.exit()

# Download the latest Paper build and save as "paper.jar"
download_latest_paper_build(mc_version, dest_folder, paper_builds_file_path)

# Start Java
start_java = f"java -Xms{min_ram}G -Xmx{max_ram}G -jar paper.jar nogui"


dl_jar(paper_builds_url, mc_paper_versions_url, dest_folder, mc_version)

# Start Java
#start_java = f"java -Xms{min_ram}G -Xmx{max_ram}G -jar paper.jar nogui"


try: 
    from GUI import mc_server_name, mc_server, mc_version, ram, eula
except ImportError and OSError as error: 
    sys.exit()



if eula == 1:
    eula = True
else:
    eula = False
    print("Did not agree to eula")
    sys.exit()




dest_folder = mc_server_name

# Set defualt ram
min_ram = ram
max_ram = ram

# Variables and calls dl_jar function

# JSON URLS
paper_builds_url = 'https://papermc.io/api/v2/projects/paper/versions/' + mc_version
mc_paper_versions_url = 'https://papermc.io/api/v2/projects/paper/'

# File names
paper_builds_filename = "Paper Builds"
mc_paper_versions_filename = "MC Paper Versions"

#File paths
paper_builds_file_path = os.path.join(dest_folder, paper_builds_filename)
mc_paper_versions_file_path = os.path.join(dest_folder, mc_paper_versions_filename)

dl_jar(paper_builds_url, mc_paper_versions_url, dest_folder, mc_version)

# Start Java
#start_java = "java -Xms" + min_ram + "G -Xmx" + max_ram + "G -jar paper.jar nogui"

# Creates batch script file

myBat = open(mc_server_name + "/start.bat",'w+')
myBat.write(start_java)
myBat.close()

# Creates shell script file
myBat = open(mc_server_name + "/" + "start.sh",'w+')
myBat.write("#!/bin/sh\n")
myBat.write('cd "$(dirname "$0")"\n')
myBat.write("")
myBat.write(start_java)
myBat.close()
#os.chmod(mc_server_name + "/start.sh", stat.S_IRWXO )

st = os.stat(mc_server_name + "/start.sh")
os.chmod(mc_server_name + "/start.sh", st.st_mode | stat.S_IEXEC)

# Saves Minecraft Server Info
file2write=open(dest_folder + "/" + "server-info.txt",'w')
file2write.write("server-name = " + mc_server_name)
file2write.write("\nmc-version = " + mc_version)
file2write.write("\nmin-ram = " + min_ram)
file2write.write("\nmax-ram = " + max_ram)
file2write.close()

if eula == True:
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



# Quit
sys.exit()