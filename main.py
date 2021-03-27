import requests
import json


# mc_version = str(input("Minecraft Version: "))


def dl_jar(mc_version):
    url = 'https://papermc.io/api/v2/projects/paper/versions/' + mc_version
    r = requests.get(url, allow_redirects=True)

    open('f.txt.json', 'wb').write(r.content)



    with open('f.txt.json', 'r') as file:
        data = file.read().replace('\n', '')


    class readjson:
        def __init__(self, json_def):
            self.__dict__ = json.loads(json_def)

    readjson = readjson(data)


    latest_build = readjson.builds[-1]

    jar_file = "paper-" + mc_version + "-" + str(latest_build) + ".jar"

    # dl_paper_jar = "https://papermc.io/api/v2/projects/paper/versions/" + str(mc_version) + "/builds/" + str(latest_build) + "/downloads/" + jar_file
    # r = requests.get(dl_paper_jar, allow_redirects=True)
    # open(jar_file, 'wb').write(r.content)

    open(jar_file, 'wb').write(r.content)

    print(url)

mc_version = str(input("Minecraft Version: "))

dl_jar(mc_version)