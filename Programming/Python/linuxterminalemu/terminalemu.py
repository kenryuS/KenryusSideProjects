#This is the linux terminal emulator written in python script using os module
import os

#setup
os.system('clear')
cmd = ""
cut = 0
directory = ""
print("Welcome to pash terminal, the bash terminal emulator written in python! The command is same to the bash. Press Ctrl + C to exit.")
print("Version: 0.0.1 alpha")

#main operation
while cut == 0:
    direct = os.popen('pwd')
    directory = direct.readline()
    cmd = input("python@pash:" + directory + ">>>")
    os.system(cmd)