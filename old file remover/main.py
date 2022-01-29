import os
import shutil
import time

def removeOldFile():
    folderName=input('choose you folder:')
    backup=input('input the backup location or type "(no backup)" to not create a backup:')
    filesList=os.listdir(folderName)

    if backup != "(no backup)":
        for file in filesList:
            shutil.copy(folderName+'/'+file,backup)
            
    


removeOldFile()