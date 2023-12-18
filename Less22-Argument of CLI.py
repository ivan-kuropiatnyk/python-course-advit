print('============Lesson22-Argument of CLI===============')
print('===========================')
import sys #imported as it is a work with system
import os

x = len(sys.argv)#sys.argv - is a massive of arguments which sends in python during a load,
#the first one (actually it is 0) will be our file.py which is loaded
#len means a length of arguments Ex.: ls -halF length of args =2="ls"+"-halF"
print("---------Print arguments as an array in the one string----")
print(sys.argv)
print("---------Print arguments starting second as an array in the string---")
print(sys.argv[1:])
print("---------Print a second and third one (the first=0 it is file)----")
print(sys.argv[1])
print(sys.argv[2])
print("---------EOF simple printing arguments")


if x > 1:#verify if a length of arguments more than 1(not 0 because the 1st is a name of a file)
    if sys.argv[1] == "/?":#if the 1st arguments is /? than print 2 lines below
        print("Help request")
        print("Usage of this prog is: python.exe argv1 argv2")
    print("Arguments entered: " + str(sys.argv[1:]))#1:-means that from a first (second after 0) till end of the string of array
else:
    print("Args not PROVIDED")

os.system("dir > test.txt")#it launch doss command dir > test.txt, means that all the output of the DIR will be written in the file test.txt
os.mkdir("MyNewDir")#creates a directorie MyNewDir, it is an exemple of the same command of upper one but in another mode of typing, like that we can launch commands in cli of windows or linux
sys.exit()#exit of the actual code (program), or stop the execution of the program
