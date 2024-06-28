

import os
import shutil

#original Downlaods path
path = "C:/Users/alefo/Downloads"

#paths for destination foleders
pptDes = "C:/Users/alefo/Downloads/Downloaded PPT"
imgDes = "C:/Users/alefo/Downloads/Downloaded Images"
pdfDes = "C:/Users/alefo/Downloads/Downloaded PDF"
vidDes = "C:/Users/alefo/Downloads/Downloaded Videos"
soundDes = "C:/Users/alefo/Downloads/Downloaded Sound"
wordDes = "C:/Users/alefo/Downloads/Downloaded WordDoc"
executeDes = "C:/Users/alefo/Downloads/Downloaded Execute"
excelDes = "C:/Users/alefo/Downloads/Downloaded Excel"


allFiles = os.listdir(path)
other = []

for file in allFiles:
    filePath = path+"/"+file
    file = file.lower()
    if file.endswith('.png') or file.endswith(".jpg") or file.endswith('.heic'):
        print("move to image folder: "+ file)
        shutil.move(filePath, imgDes)
    elif file.endswith('.pdf'):
        print("move to pdf folder: "+ file)
        shutil.move(filePath, pdfDes)
    elif file.endswith('.mov') or file.endswith('.mp4'):
        print("move to video folder: "+file)
        shutil.move(filePath, vidDes)
    elif file.endswith('.pptx'):
        print("move to ppt folder: "+file)
        shutil.move(filePath, pptDes)
    elif file.endswith('.mp3'):
        print("move to sound folder: "+file)
        shutil.move(filePath, soundDes)
    elif file.endswith('.docx') or file.endswith('.doc'):
        print("move to doc folder: "+file)
        shutil.move(filePath, wordDes)
    elif file.endswith('.exe'):
        print("move to exe folder: "+file)
        shutil.move(filePath, executeDes)
    elif file.endswith('.xlsx'):
        print("move to excel folder: "+file)
        shutil.move(filePath, excelDes)
    else:
        other.append(file)
    
if other:
    print("THESE FILES ARE NOT ORGANIZED")
    for file in other:
        print(file)

