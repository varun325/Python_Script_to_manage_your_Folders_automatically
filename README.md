# Python Script to manage your folders automatically
## _This Script can run in back ground add move files to differemt folders based upon file types_

**In this example we have managed the download folder**

*Custom editing steps:*
* *Change folder = "/Downloads to folder = "/Yoour/file/path" for your custom folder management*
* *You can add extra conditions or modify the existing ones and change the folder names if you know your way arounf python*

**Making the script run in background**
* we are using crontab to run script in background 
* copy the contents to /bin
    * ``` console user@machine:~$sudo cp -i /your/file/path/watch.py /bin ```
* open crontab, select 1 to 4 if you haven't assigned any
    * ``` console
        user@machine:~$sudo crontab -e
        ```
* Add the given  line to your crontab
    * ``` console @reload sudo -u username python3 /bin/watch.py```
