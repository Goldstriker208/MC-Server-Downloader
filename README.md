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
## Run MC Server Downloader  
CLI:      
```python CLI.py```  

GUI:    
```python dl_paper_jar.py```  
  
# Dependencies for Linux  
## Arch  
```sudo pacman -S tk```  
## Debian  
```sudo apt-get install python-tk```  
  

# Run MC Server Downloader on iOS (Jailbreak Required)
## Install Required Tweaks 
Install these tweaks on Cydia or Sileo:   
[NewTerm 2](https://chariz.com/get/newterm) (Chariz Repo)  
[Filza File Manager](http://cydia.saurik.com/package/com.tigisoftware.filza/) (Big Boss Repo)  
[OpenJDK 16 - Runtime](https://doregon.github.io/cydia) (Doregon's Repo)  
Git (Sam Bingner's Repo)   
OpenSSH (Sam Bingner's Repo)   
nano (Sam Bingner's Repo)
Python 3.7  

Doregon's Repo:  https://doregon.github.io/cydia

## Run MC Server Downloader on iOS Terminal
1. Open NewTerm 2
2. Become super user type ```su``` Default password: alpine
3. Edit /etc/profile in nano  ```nano /etc/profile```
4. Set Java PATH: add /usr/lib/jvm/java-16-openjdk/bin/ to PATH Variable
5. Save and Quit
6. ```git clone https://github.com/Goldstriker208/MC-Server-Downloader.git```
7. Change directory to ```cd MC-Server-Downloader```
8. Run the MC Server Downloader by typing in ```python3 CLI.py```

## Run MC Server Downloader Via SSH (recommended)
In macOS/Linux Terminal type:
```ssh mobile@your-device's-local-ip```   

On Windows use the program [PuTTY](https://www.putty.org/) 

Hostname: Your device's local ip  
Login: mobile  
Default Password: alpine  

Repeat the same steps as on NewTerm 2  
