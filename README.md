
# Python Script to manage your folders automatically
## _This Script can run in back ground and move files to different folders based upon file types_

**In this example we have managed the download folder**

*Custom editing steps:*
* ```python
     #change
     folder = "/Downloads"
     #to
     folder = "/Your/folder"
     ```
* *You can add extra conditions or modify the existing ones and change the folder names if you know your way around python  for. example:*
    * ```python

        folder ="/Downloads"
        #folder ="/Your/folder"
        home = Path.home()
        
        #Replace "/Books" with the destination folder
        #You can also replace books with a different variable name
        if not os.path.exists(str(home)+folder+"/Books"):
            os.makedirs(str(home)+folder+"/Books")

        book = str(home)+folder+"/Books"
        #instead of ".epub", you can mention other formats as well
        files = [i for i in os.listdir(src) if path.isfile(path.join(src, i))]
        for f in files:
            if f.endswith(".epub") or f.endswith(".EPUB"):
                shutil.move(path.join(src, f), path.join(book,f))
        ```

## Making the script run in background(LINUX {UBUNTU})

*we are using crontab to run script in background* 
* [x] copy the contents to /bin
    * ``` sh
        user@machine:~$ sudo cp -i /your/file/path/watch.py /bin 
        ```
* [x] open crontab, select 1 to 4 if you haven't assigned any
    * ``` bash
        user@machine:~$ sudo crontab -e
        ```
* [x] Add the given  line to your crontab
    * ``` bash 
        @reboot sudo -u username python3 /bin/watch.py
        ```
* [x] Reboot the system
    * ```bash
        user@machine:~$ reboot
        ```
## Making the script run in background(Windows)

*we are using pythonw.exe to run script in background* 
* [x] copy the watchWin.pyw to
     * ```bash
          C:\Users\current_user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\
          ```
* [x] run ```%appdata``` if you can't find AppData in User directory
* [x] add file to the windows registry folder by running the appRegistry.py script
    * ```bash
         C:\Your\File\Path> python3 appRegistry.py
         ```
* [ ] on startup windows will execute (Windows does this automatically, it's here just for explanation)
     * ```bash
          C:\Users\current_user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup> pythonw.exe watchWin.pyw
          ```
* [x] Reboot the system
>Happy Scripting :computer: :heart:
