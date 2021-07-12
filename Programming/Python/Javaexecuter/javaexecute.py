#Java executer written in Python
import os
x = 0
while x == 0:
    path = ""
    command = ""
    errorind = ""
    path = input('path to the java file: ')
    command = "javac " + path
    print("compiling code...")
    os.system(command)
    print("Running the code...")
    command = "java " + path
    os.system(command)
    input("Press enter to continue.")
    os.system('cls')
