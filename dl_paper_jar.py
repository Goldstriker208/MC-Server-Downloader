import requests
import json
import os
import sys
import stat
import shutil
import subprocess
from sys import platform
import time
import urllib.request
from urllib.error import HTTPError, URLError

class MinecraftServerSetup:
    def __init__(self, mc_server_name, mc_version, ram, eula):
        self.mc_server_name = mc_server_name
        self.mc_version = mc_version
        self.ram = ram
        self.eula = eula

        # File names
        self.paper_builds_filename = "Paper Builds"
        self.mc_paper_versions_filename = "MC Paper Versions"

        # File paths
        self.paper_builds_file_path = os.path.join(self.mc_server_name, self.paper_builds_filename)
        self.mc_paper_versions_file_path = os.path.join(self.mc_server_name, self.mc_paper_versions_filename)

        # URLs
        self.paper_builds_url = f'https://papermc.io/api/v2/projects/paper/versions/{self.mc_version}'
        self.mc_paper_versions_url = 'https://papermc.io/api/v2/projects/paper/'

        # Variables
        self.min_ram = self.ram
        self.max_ram = self.ram
        self.mc_paper_versions = None
        self.readjson_paper_builds = None

    def create_server_folder(self):
        if not os.path.exists(self.mc_server_name):
            os.makedirs(self.mc_server_name)
            print("Created Folder:", self.mc_server_name)

    def download_json(self, url, filename, file_path):
        r = requests.get(url, allow_redirects=True)
        print(f"Downloaded File: JSON {filename}")
        open(file_path, 'wb').write(r.content)
        print(f"Saved JSON {filename} to", os.path.abspath(file_path))
        with open(file_path, 'r') as file:
            return file.read().replace('\n', '')

    def read_json(self, json_data):
        class ReadJson:
            def __init__(self, json_def):
                self.__dict__ = json.loads(json_def)
        return ReadJson(json_data)

    def dl_jar(self):
        # Create Minecraft Server folder
        self.create_server_folder()

        # Download Paper Builds JSON
        paper_builds_data = self.download_json(self.paper_builds_url, self.paper_builds_filename,
                                               self.paper_builds_file_path)

        # Download Paper MC Versions JSON
        mc_paper_versions_data = self.download_json(self.mc_paper_versions_url, self.mc_paper_versions_filename,
                                                    self.mc_paper_versions_file_path)

        # Read JSON Files
        self.readjson_paper_builds = self.read_json(paper_builds_data)
        readjson_paper_versions = self.read_json(mc_paper_versions_data)

        self.mc_paper_versions = readjson_paper_versions.versions + readjson_paper_versions.version_groups

        # Return mc_paper_versions and readjson_paper_builds
        return self.mc_paper_versions, self.readjson_paper_builds

    def download_latest_paper_build(self):
        # Get the latest build number
        latest_build = self.readjson_paper_builds.builds[-1]
        print("Downloading Latest Build:", latest_build)
        jar_file = f"paper-{self.mc_version}-{latest_build}.jar"
        dl_paper_jar = f"https://papermc.io/api/v2/projects/paper/versions/{self.mc_version}/builds/{latest_build}/downloads/{jar_file}"
        r = requests.get(dl_paper_jar, allow_redirects=True)
        print("Downloaded:", jar_file)

        # Save the JAR file
        jar_path = os.path.join(self.mc_server_name, jar_file)
        open(jar_path, 'wb').write(r.content)
        print("Saved", jar_file, "to", os.path.abspath(jar_path))

        # Rename to "paper.jar"
        os.rename(jar_path, os.path.join(self.mc_server_name, "paper.jar"))

    def check_valid_mc_version(self):
        for mc_paper_version in self.mc_paper_versions:
            if self.mc_version == mc_paper_version:
                print("Valid MC Paper Version")
                return True
        return False

    def start_server(self):
        # Start Java
        start_java = f"java -Xms{self.min_ram}G -Xmx{self.max_ram}G -jar paper.jar nogui"

        # Creates batch script file
        with open(os.path.join(self.mc_server_name, "start.bat"), 'w+') as my_bat:
            my_bat.write(start_java)

        # Creates shell script file
        with open(os.path.join(self.mc_server_name, "start.sh"), 'w+') as my_bat:
            my_bat.write("#!/bin/sh\n")
            my_bat.write(f'cd "$(dirname "$0")"\n\n')
            my_bat.write(start_java)

        st = os.stat(os.path.join(self.mc_server_name, "start.sh"))
        os.chmod(os.path.join(self.mc_server_name, "start.sh"), st.st_mode | stat.S_IEXEC)

        # Saves Minecraft Server Info
        with open(os.path.join(self.mc_server_name, "server-info.txt"), 'w') as file2write:
            file2write.write(f"server-name = {self.mc_server_name}\n")
            file2write.write(f"mc-version = {self.mc_version}\n")
            file2write.write(f"min-ram = {self.min_ram}\n")
            file2write.write(f"max-ram = {self.max_ram}\n")

        if self.eula:
            with open(os.path.join(self.mc_server_name, "eula.txt"), 'w') as file2write:
                file2write.write("eula=true\n")

        print("Open the batch script or shell script file to start your Minecraft Server")
        print(os.path.abspath(self.mc_server_name))

        time.sleep(1)
        os.system(f"cd {os.path.abspath(self.mc_server_name)}")

        # if platform == "win32":
        #     subprocess.Popen(f"explorer /select,{os.path.abspath(self.mc_server_name)}")
        if platform == "win32":
            explorer_command = f"explorer /select,{os.path.abspath(self.mc_server_name)}"
            subprocess.Popen(explorer_command, shell=True)

            # Wait for the File Explorer to open
            time.sleep(2)

            # Execute the start.bat file
            start_bat_path = os.path.join(self.mc_server_name, "start.bat")
            subprocess.Popen([start_bat_path], shell=True)

        sys.exit()

if __name__ == "__main__":
    try:
        from GUI import mc_server_name, mc_version, ram, eula
    except ImportError and OSError as error:
        sys.exit()

    minecraft_server_setup = MinecraftServerSetup(
        mc_server_name=mc_server_name,
        mc_version=mc_version,
        ram=ram,
        eula=eula
    )

    mc_paper_versions, readjson_paper_builds = minecraft_server_setup.dl_jar()

    if not minecraft_server_setup.check_valid_mc_version():
        print("Invalid MC Version")
        sys.exit()

    minecraft_server_setup.download_latest_paper_build()

    minecraft_server_setup.start_server()
