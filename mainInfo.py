import requests

mc_version = "1.16.5"

url = 'https://papermc.io/api/v2/projects/paper/versions/' + mc_version
r = requests.get(url, allow_redirects=True)

open('f.txt.json', 'wb').write(r.content)

print("Paper URL JSON: " + url)

import json

with open('f.txt.json', 'r') as file:
    data = file.read().replace('\n', '')

print("JSON file text: " + data)


class readjson:
    def __init__(self, json_def):
        self.__dict__ = json.loads(json_def)

readjson = readjson(data)

print("project_id: " + readjson.project_id)
print("project_name: " + readjson.project_name)
print("version: " + readjson.version)
print("builds: " + str(readjson.builds))

print("Latest Build: " + str(readjson.builds[-1]))

latest_build = readjson.builds[-1]

jar_file = "paper-1.16.5-" + str(latest_build) + ".jar"

# dl_paper_jar = "https://papermc.io/api/v2/projects/paper/versions/" + str(mc_version) + "/builds/" + str(latest_build) + "/downloads/" + jar_file
# r = requests.get(dl_paper_jar, allow_redirects=True)
# open(jar_file, 'wb').write(r.content)

open(jar_file, 'wb').write(r.content)

print(url)
