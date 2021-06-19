# Minecraft Server Downloader
## Install Required Python Modules
### Windows
  ```sh
    pip install -r requirements.txt
  ```
### macOS/Linux/iOS
  ```sh
    pip3 install -r requirements.txt
  ```

## Install Required Tweaks (iOS Jailbreak Only)
Install these tweaks on Cydia or Sileo:  
[NewTerm 2](https://chariz.com/get/newterm)  
[Filza File Manager](http://cydia.saurik.com/package/com.tigisoftware.filza/)   
[OpenJDK 16 - Runtime](https://doregon.github.io/cydia)   
Git  
OpenSSH (optional but recommend)  

OpenJDK 16 / PojavLauncher Repo:  https://doregon.github.io/cydia

1. Open NewTerm 2
2. Become Super User type ```su``` Defualt password: alpine
3. Edit /etc/profile in nano  ```nano /etc/profile```
4. Set Java PATH: add /usr/lib/jvm/java-16-openjdk/bin/ to PATH Variable
5. Save and Quit
6. ```git clone https://github.com/Goldstriker208/MC-Server-Downloader.git```
7. 
