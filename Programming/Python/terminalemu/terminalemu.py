#This is the linux terminal emulator written in python script using os module
import os

#setup
path= ""
cmd = ""
cut = 0
version = "Version: 0.0.8 alpha"
print("Welcome to Pyminal, the terminal emulator written in python!")
print("The commands are same to the bash and windows cmd. Type [pelp] for more information.")
print(version)

#main operation
while cut == 0:
    cmd = input("python@localfile; pyminal:>>> ")
    #custom command cmd command indicator
    if cmd == "version":
        print(version)
    elif cmd == "exit":
        print("exitting from Pyminal ...")
        break
    elif cmd == "clog":
        print(version)
        print("1. add the error message instead closing when you using pcd command")
        print("2. changed the name to Pyminal")
    elif cmd == "pcd":
        path = input("Where is the destination of the working directory:")
        try:
            os.chdir(path)
            print("Current working directory: {0}".format(os.getcwd()))
        except FileNotFoundError:
            print("Directory: {0} does not exist".format(path))
        except NotADirectoryError:
            print("{0} is not a directory".format(path))
        except PermissionError:
            print("You do not have permissions to change to {0}".format(path))
    elif cmd == "pelp":
        print("This is the python program that excecute the bash and windows cmd commands.")
        print("Here are the some commands that only for this terminal emulator.")
        print("[version] - shows the version of the pash terminal")
        print("[exit] - exit the Pyerminal")
        print("[pelp] - shows the help of the pash terminal")
        print("[clog] - show the change log of Pyminal")
        print("[pcd] - change the working directory")
        print("Note: You can't use the cd command. Instead, use pcd command.")
        print("")
        print("Updated: 5/3/2021 by kenryuS. Opensource project on github")
    else:
        os.system(cmd)