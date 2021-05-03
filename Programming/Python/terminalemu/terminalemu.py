#This is the linux terminal emulator written in python script using os module
import os

#setup
pcd = ""
cmd = ""
cut = 0
version = "Version: 0.0.7 alpha"
print("Welcome to pash terminal, the bash terminal emulator written in python!")
print("The commands are same to the bash. Type [pelp] for more information.")
print(version)

#main operation
while cut == 0:
    cmd = input("python@pash:>>>")
    #custom command cmd command indicator
    if cmd == "version":
        print(version)
    elif cmd == "exit":
        print("exitting from pash ...")
        break
    elif cmd == "clog":
        print("version 0.0.7 alpha;")
        print("1. add the pcd command which change the working directory")
    elif cmd == "pcd":
        pcd = input("Where is the destination of the working directory:")
        os.chdir(pcd)
    elif cmd == "pelp":
        print("This is the python program that excecute the bash commands.")
        print("Here are the some commands that only for this terminal emulator.")
        print("[version] - shows the version of the pash terminal")
        print("[exit] - exit the pash terminal")
        print("[pelp] - shows the help of the pash terminal")
        print("[clog] - show the change log of the pash")
        print("Note: You can't use the cd command. instead use the pcd.")
        print("")
        print("Update: 5/3/2021 by kenryuS")
    else:
        os.system(cmd)