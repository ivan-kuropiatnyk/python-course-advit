#!/bin/python3 #############for using in linux

import shutil   #For CopyFile
import os       #For GetFilesize and check if file exist
import sys      #For CLI Arguments

# lesson-4-putgelog.py mylog.txt 10(size in kbites) 5(quantity of files)

if(len(sys.argv) < 4):
    print("Missing arguments! Usage is script.py 10 5")
    exit(1)#exit with an error code 1

file_name = sys.argv[1]
limitsize = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name) == True):          # Check if MAIN log file exists
    log_file_size = os.stat(file_name).st_size  # Check a size of the file
    log_file_size = log_file_size / 1024        #convert from bytes to kylobytes

    if (log_file_size >= limitsize):
        if(logsnumber > 0):
            for currentFileNum in range(logsnumber, 1, -1):
                src = file_name + "_" + str(currentFileNum-1)
                dst = file_name + "_" + str(currentFileNum)
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)
                    print("File copied from:" + src + " to " + dst)

            shutil.copyfile(file_name, file_name + "_1")
            print("Copied: " + file_name + "  to  " + file_name + "_1")

        myfile = open(file_name, 'w')
        myfile.close()