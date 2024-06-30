

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime


class FileMoverHandler(FileSystemEventHandler):
    def __init__(self):
        self.path = "C:/Users/alefo/Downloads"
        self.pptDes = "C:/Users/alefo/Downloads/Downloaded PPT"
        self.imgDes = "C:/Users/alefo/Downloads/Downloaded Images"
        self.pdfDes = "C:/Users/alefo/Downloads/Downloaded PDF"
        self.vidDes = "C:/Users/alefo/Downloads/Downloaded Videos"
        self.soundDes = "C:/Users/alefo/Downloads/Downloaded Sound"
        self.wordDes = "C:/Users/alefo/Downloads/Downloaded WordDoc"
        self.executeDes = "C:/Users/alefo/Downloads/Downloaded Execute"
        self.excelDes = "C:/Users/alefo/Downloads/Downloaded Excel"

    def move_file(self, filePath, dest, file):
        base, extension = os.path.splitext(filePath)
        destPath = os.path.join(dest, os.path.basename(filePath))

        if os.path.exists(destPath):
            print("Path: "+ destPath + " already exists!")
            timestamp = datetime.now().strftime('%y_%m_%d_%I_%M_%S')
            # destPath = os.path.join(dest, f"{os.path.basename(base)}_{timestamp}{extension}")
            destPath = dest+ "/"+ f"{os.path.basename(base)}_{timestamp}{extension}"
            print("Path changed to: "+ destPath )

        print('MOVING: "' + file +'" --> "'+destPath+'"')
        shutil.move(filePath, destPath)
    
    def on_created(self, event):
        if event.is_directory:
            return
        
        filePath = event.src_path

        file = os.path.basename(filePath).lower()
        allFiles = os.listdir(path)
        other = []

        for file in allFiles:
            filePath = path+"/"+file
            file = file.lower()

            if file.endswith('.png') or file.endswith(".jpg") or file.endswith('.heic') or file.endswith('.gif'):
                self.move_file(filePath, self.imgDes, file)
            elif file.endswith('.pdf'):
                print("move to pdf folder: " + file)
                self.move_file(filePath, self.pdfDes, file)
            elif file.endswith('.mov') or file.endswith('.mp4'):
                print("move to video folder: " + file)
                self.move_file(filePath, self.vidDes, file)
            elif file.endswith('.pptx'):
                print("move to ppt folder: " + file)
                self.move_file(filePath, self.pptDes, file)
            elif file.endswith('.mp3'):
                print("move to sound folder: " + file)
                self.move_file(filePath, self.soundDes, file)
            elif file.endswith('.docx') or file.endswith('.doc'):
                print("move to doc folder: " + file)
                self.move_file(filePath, self.wordDes, file)
            elif file.endswith('.exe'):
                print("move to exe folder: " + file)
                self.move_file(filePath, self.executeDes, file)
            elif file.endswith('.xlsx'):
                print("move to excel folder: " + file)
                self.move_file(filePath, self.excelDes, file)
            else:
                
                if ("downloaded" not in file) and (".tmp" not in file):
                    # print(file)
                    other.append(file)
        
        if other: 
            print("THESE FILES ARE NOT ORGANIZED:")
            print(other)

if __name__ == "__main__":
    path = "C:/Users/alefo/Downloads"
    event_handler = FileMoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()