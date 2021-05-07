#This is the unix/windows cmd terminal emulator written in python script using os module
import os

#startup
path= ""
cmd = ""
version = "Version: 0.0.9.2 alpha"
cut = 0
pelpc = 0
welcomec = 0
clogc = 0
hisc = 0
pathb = []
pelp = ["This is the python program that execute the bash and windows cmd commands", "Here are the some commands that only for this terminal emulator.", "[version] - shows the version of the pash terminal", "[exit] - exit the Pyerminal", "[pelp] - shows the help of the pash terminal", "[clog] - show the change log of Pyminal", "[history] - show the command history you typed in.", "[hisclear] - clear the command history.", "[pcd] - change the working directory", "Note: You can't use the cd command. Instead, use pcd command.", "", "Updated: 5/4/2021 by kenryuS. Opensource project on github"]
welcome = ["Welcome to Pyminal, the terminal emulator written in python!", "Ther commands are same to the bash or windows cmd. Type [pelp] for more information.", version]
clog = [version, "1. made the pcd command more easily"]
history = []
while welcomec <= (len(welcome) - 1):
    print(welcome[welcomec])
    welcomec += 1

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
        while clogc <= (len(clog) - 1):
            print(clog[clogc])
            clogc += 1
        clogc = 0
    elif cmd == "history":
        while hisc <= (len(history) - 1):
            print(history[hisc])
            hisc += 1
        hisc = 0
    elif cmd == "hisclear":
        history.clear()
    elif ('pcd' in cmd) == True:
        pathb = cmd.split(' ', 1)
        path = pathb[1]
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
        while pelpc <= (len(pelp) - 1):
            print(pelp[pelpc])
            pelpc += 1
        pelpc = 0
    else:
        os.system(cmd)
    history.append(cmd)