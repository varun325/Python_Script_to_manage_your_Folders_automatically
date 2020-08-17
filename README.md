// colors
s {color:orange}
# Python Script to manage your folders automatically
## _This Script can run in back ground add move files to differemt folders based upon file types_

**In this example we have managed the download folder**

*Custom editing steps:*
* *Change `python folder = "/Downloads` to `python folder = "/Yoour/file/path"` for your custom folder management*
* *You can add extra conditions or modify the existing ones and change the folder names if you know your way around python  for. example:*
    * ```python

        folder ="/Downloads"
        home = Path.home()

        if not os.path.exists(str(home)+folder+"/Books"):
            os.makedirs(str(home)+folder+"/Books")

        book = str(home)+folder+"/Books"

        files = [i for i in os.listdir(src) if path.isfile(path.join(src, i))]
        for f in files:
            if f.endswith(".epub") or f.endswith(".EPUB"):
                shutil.move(path.join(src, f), path.join(book,f))
        ```

**Making the script run in background**
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
        @reload sudo -u username python3 /bin/watch.py
        ```
* [x] Reboot the system
    * ```bash
        ~~*user@machine:~*~~$ reboot
        ```
