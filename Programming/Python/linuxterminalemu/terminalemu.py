#This is the linux terminal emulator written in python script using os module
import os

#setup
os.system('clear')
cmd = ""
cut = 0
directory = ""
print("Welcome to pash terminal, the bash terminal emulator written in python! The command is same to the bash. Press Ctrl + C to exit.")

#main operation
while cut == 0:
    direct = os.popen('pwd')
    directory = direct.readline()
    cmd = input("python@bash:" + directory + ">>>")
    os.system(cmd)