#!/bin/python3 #############for using in linux

import os, time   #time - For a work with time
      #os - For GetFilesize and check if file exist

DAYS = 5    #Maximal age of file to stay
FOLDERS = [
    "D:\Musorka\Hlam",
    "D:\Musorka\Musor",
    "D:\Musorka\Raznoe",
    ]

TOTAL_DELETED_SIZE = 0      #Total deleted size of files
TOTAL_DELETED_FILE = 0     #Total deleted files
TOTAL_DELETED_DIRS = 0      #Total deleted folgers

nowTime = time.time() #get time in seconds
ageTime = nowTime - 60*60*24*DAYS #Minus days in seconds

def delete_old_files(folder):
    """Delete files older than X DAYS"""
    global TOTAL_DELETED_SIZE
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_DIRS
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file) #get ful path in the file
            filePath = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile      #Count sum of all free space
                TOTAL_DELETED_file += 1             # Count number of deleted files
                print("Deleting files:" + str(fileName))
                os.remove(fileName)                 #Delete file

def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    empty_folder_in_this_run = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            empty_folder_in_this_run += 1
            print("Deleting empty folders: " + str(path))
            os.rmdir(path)
    if empty_folder_in_this_run > 0:
        delete_empty_dir(folder)

#==========MAIN============
starttime = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)
    delete_empty_dir(folder)

finishtime = time.asctime()

print("-----------------------------")
print("START TIME:" + str(starttime))
print("Total deleted size = " + str(int(TOTAL_DELETED_SIZE/1024/1024)) + "MB")
print("Total deleted files = " + str(TOTAL_DELETED_FILE))
print("Total deleted folders = " + str(TOTAL_DELETED_DIRS))
print("FINISH TIME:" + str(finishtime))
print("-----------EOF---------------")