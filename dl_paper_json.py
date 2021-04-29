import requests
import json
import os
import sys
import shutil
import subprocess
import time


from GUI import mc_version

dest_folder = "jsons"

os.mkdir(dest_folder)






# Variables and calls dl_jar function

# JSON URLS
mc_paper_versions_url = 'https://papermc.io/api/v2/projects/paper/'

# File names
mc_paper_versions_filename = "MC Paper Versions"

#File paths
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


# Read JSON Files
class readjson:
    def __init__(self, json_def):
        self.__dict__ = json.loads(json_def)

readjson_paper_versions = readjson(mc_paper_versions_data)

global mc_paper_versions
mc_paper_versions = readjson_paper_versions.versions + readjson_paper_versions.version_groups


def check_vaild_mc_version():
    vaild_mc_version = None
    for mc_paper_version in mc_paper_versions:
        if mc_version == mc_paper_version:
            vaild_mc_version = True
            print("Vaild MC Paper Version")
            return True

    if mc_version != mc_paper_version: 
        return False
        sys.exit()
        

if check_vaild_mc_version() == True:
    pass


else:
    print("Invaild MC Version")









# Quit
sys.exit()