from dl_paper_jar import server_name
def startbat():
    myBat = open(server_name + "/" + "start.bat",'w+')

    myBat.write("java -Xms2G -Xmx2G -jar Spigot-1.10.2.jar nogui")

    myBat.close()