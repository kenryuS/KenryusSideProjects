#This is the unix/windows cmd terminal emulator written in python script using os module
import os

#startup
sys = ""
pindi = ""
path= ""
cmd = ""
version = "Version: 0.0.9.3 alpha"
cut = 0
pelpc = 0
welcomec = 0
clogc = 0
hisc = 0
pathb = []
pelp = ["This is the python program that execute the bash and windows cmd commands", "Here are the some commands that only for this terminal emulator.", "[exit] - exit the Pyerminal", "[pelp] - shows the help of the pash terminal", "[clog] - show the change log of Pyminal", "[history] - show the command history you typed in.", "[hisclear] - clear the command history.", "[pcd] - change the working directory", " ", "Updated: 5/10/2021 by kenryuS. Opensource project on github"]
welcome = ["Welcome to Pyminal, the terminal emulator written in python!", "Ther commands are same to the bash or windows cmd. Type [pelp] for more information.", version]
clog = [version, "1. deleated version command", "2. changed the input prompt"]
history = []
while welcomec <= (len(welcome) - 1):
    print(welcome[welcomec])
    welcomec += 1

#main operation
sys = input("OS cmd setting[Linux or Windows]")
while cut == 0:
    if sys == "Windows":
        pindi = os.popen('echo %cd%').read()
        pindi = pindi[0:-1]
    elif sys == "Linux":
        pindi = os.popen('pwd').read()
        pindi = pindi[0:-1]
    
    cmd = input("python@pyminal " + pindi + ":>>> ")
    #custom command cmd command indicator
    if cmd == "exit":
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