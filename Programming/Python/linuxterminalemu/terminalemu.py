#This is the linux terminal emulator written in python script using os module
import os

#setup variable
cmd = ""
cut = 0

#main operation
while cut == 0:
    cmd = input("python@bash: >>>")
    os.system(cmd)