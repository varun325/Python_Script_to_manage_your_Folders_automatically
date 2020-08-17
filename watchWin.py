#!/usr/bin/env python3
import time 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
import os
from os import path
from pathlib import Path
import errno
import shutil
# print("hello")
folder ="\Downloads"
home = Path.home()
print(str(Path.home()))
if not os.path.exists(str(home)+folder+"\Docs"):
    os.makedirs(str(home)+folder+"\Docs")
if not os.path.exists(str(home)+folder+"\Pdfs"):
    os.makedirs(str(home)+folder+"\Pdfs")
if not os.path.exists(str(home)+folder+"\Images"):
    os.makedirs(str(home)+folder+"\Images")
if not os.path.exists(str(home)+"\Desktop\Wallpapers"):
    os.makedirs(str(home)+"\Desktop\Wallpapers")
if not os.path.exists(str(home)+folder+"\Zips"):
    os.makedirs(str(home)+folder+"\Zips")
if not os.path.exists(str(home)+folder+"\Ppts"):
    os.makedirs(str(home)+folder+"\Ppts")
if not os.path.exists(str(home)+folder+"\Videos"):
    os.makedirs(str(home)+folder+"\Videos")
if not os.path.exists(str(home)+folder+"\Music"):
    os.makedirs(str(home)+folder+"\Music")
if not os.path.exists(str(home)+folder+"\Jupiter"):
    os.makedirs(str(home)+folder+"\Jupiter")
if not os.path.exists(str(home)+folder+"\Xlsx"):
    os.makedirs(str(home)+folder+"\Xlsx")
if not os.path.exists(str(home)+folder+"\Web"):
    os.makedirs(str(home)+folder+"\Web")
if not os.path.exists(str(home)+folder+"\Java"):
    os.makedirs(str(home)+folder+"\Java")
if not os.path.exists(str(home)+folder+"\Python"):
    os.makedirs(str(home)+folder+"\Python")
if not os.path.exists(str(home)+folder+"\Torrents"):
    os.makedirs(str(home)+folder+"\Torrents")
if not os.path.exists(str(home)+folder+"\Apks"):
    os.makedirs(str(home)+folder+"\Apks")
if not os.path.exists(str(home)+folder+"\Books"):
    os.makedirs(str(home)+folder+"\Books")
def movement():
    home = Path.home()
    src = str(home)+folder
    doc = str(home)+folder+"\Docs"
    pdf = str(home)+folder+"\Pdfs"
    images = str(home)+folder+"\Images"
    wall = str(home)+"\Desktop\Wallpapers"
    zips = str(home)+folder+"\Zips"
    pptx = str(home)+folder+"\Ppts"
    vids = str(home)+folder+"\Videos"
    music = str(home)+folder+"\Music"
    jupiter = str(home)+folder+"\Jupiter"
    excel = str(home)+folder+"\Xlsx"
    web = str(home)+folder+"\Web"
    java = str(home)+folder+"\Java"
    python = str(home)+folder+"\Python"
    torrent = str(home)+folder+"\Torrents"
    apk = str(home)+folder+"\Apks"
    book = str(home)+folder+"\Books"
    files = [i for i in os.listdir(src) if path.isfile(path.join(src, i))]
    for f in files:
        if f.endswith("-unsplash.jpg"):
            shutil.move(path.join(src, f), path.join(wall,f))
        elif f.endswith(".jpg") or f.endswith(".png") or f.endswith(".PNG") or f.endswith(".JPG")  or f.endswith(".JEPG")  or f.endswith(".jpeg"):
            shutil.move(path.join(src, f), path.join(images,f))
        elif f.endswith(".py") or f.endswith(".PY"):
            shutil.move(path.join(src, f), path.join(python,f))
        elif f.endswith(".epub") or f.endswith(".EPUB"):
            shutil.move(path.join(src, f), path.join(book,f))
        elif f.endswith(".apk") or f.endswith(".APK"):
            shutil.move(path.join(src, f), path.join(apk,f))
        elif f.endswith(".java") or f.endswith(".JAVA"):
            shutil.move(path.join(src, f), path.join(java,f))
        elif f.endswith(".torrent") or f.endswith(".TORRENT"):
            shutil.move(path.join(src, f), path.join(torrent,f))
        elif f.endswith(".pdf") or f.endswith(".PDF"):
            shutil.move(path.join(src, f), path.join(pdf,f))
        elif f.endswith(".doc") or f.endswith(".docx") or f.endswith(".DOC") or f.endswith(".DOCX"):
            shutil.move(path.join(src, f), path.join(doc,f))
        elif f.endswith(".zip") or f.endswith(".gz") or f.endswith(".xz") or f.endswith(".ZIP") or f.endswith(".exe") or f.endswith(".EXE") or f.endswith(".7z") or f.endswith(".7Z") or f.endswith(".GZ") or f.endswith(".XZ") or f.endswith(".deb") or f.endswith(".DEB") or f.endswith("bz2") or f.endswith(".BZ2"):
            shutil.move(path.join(src, f), path.join(zips,f))
        elif f.endswith(".ppt") or f.endswith(".pptx") or f.endswith(".PPT") or f.endswith(".PPTX"):
            shutil.move(path.join(src, f), path.join(pptx,f))
        elif f.endswith(".mp3") or f.endswith(".odd") or f.endswith(".MP3") or f.endswith(".ODD"):
            shutil.move(path.join(src, f), path.join(music,f))
        elif f.endswith(".mp4") or  f.endswith(".MP4"):
            shutil.move(path.join(src, f), path.join(vids,f))
        elif f.endswith(".ipynb") or f.endswith(".IPYNB"):
            shutil.move(path.join(src, f), path.join(jupiter,f))
        elif f.endswith(".xls") or f.endswith(".xlsx") or f.endswith(".XLS") or f.endswith(".XLSX"):
            shutil.move(path.join(src, f), path.join(excel,f))
        elif f.endswith(".html") or f.endswith(".js") or f.endswith(".json") or f.endswith(".JSON") or f.endswith(".HTML") or f.endswith(".JS") or f.endswith(".CSS") or f.endswith(".css") or f.endswith(".php") or f.endswith(".PHP"):
            shutil.move(path.join(src, f), path.join(web,f))
    
class OnMyWatch: 
    # Set the directory on watch 
    watchDirectory = str(home)+folder
  
    def __init__(self): 
        self.observer = Observer() 
  
    def run(self): 
        event_handler = Handler() 
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True) 
        self.observer.start() 
        try: 
            while True: 
                time.sleep(5) 
        except: 
            self.observer.stop() 
            print("Observer Stopped") 
  
        self.observer.join() 
  
  
class Handler(FileSystemEventHandler): 
    
    @staticmethod
    def on_any_event(event): 
        if event.is_directory: 
            return None
  
        elif event.event_type == 'created': 
            # Event is created, you can process it now 
            movement()
            print("Watchdog received created event - % s." % event.src_path) 
        elif event.event_type == 'moved': 
            # Event is created, you can process it now 
            movement()
            print("Watchdog received move event - % s." % event.src_path) 
              
  
if __name__ == '__main__': 
    watch = OnMyWatch() 
    watch.run() 