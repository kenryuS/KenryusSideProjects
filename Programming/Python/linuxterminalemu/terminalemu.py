#This is the linux terminal emulator written in python script using os module
import os

#setup
os.system('clear')
cmd = ""
cut = 0
directory = ""
version = "Version: 0.0.5 alpha"
print("Welcome to pash terminal, the bash terminal emulator written in python!")
print("The commands are same to the bash. Type [pelp] for more information.")
print(version)

#main operation
while cut == 0:
    direct = os.popen('pwd')
    directory = direct.readline()
    cmd = input("python@pash:" + directory + ">>>")
    if cmd == "version":
        print(version)
    elif cmd == "exit":
        print("exitting from pash ...")
        break
    elif cmd == "pelp":
        print("This is the python program that excecute the bash commands.")
        print("Here are the some commands that only for this terminal emulator.")
        print("[version] - shows the version of the pash terminal")
        print("[exit] - exit the pash terminal")
        print("[pelp] - shows the help of the pash terminal")
        print("")
        print("Update: 5/1/2021 by kenryuS")
    else:
        os.system(cmd)