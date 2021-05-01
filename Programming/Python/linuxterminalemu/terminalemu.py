#This is the linux terminal emulator written in python script using os module
import os

#setup
cmd = ""
cut = 0
direct = ""
os.system('cd $HOME')

#main operation
while cut == 0:
    direct = os.system('pwds')
    cmd = input("python@bash:" + direct + ">>>")
    os.system(cmd)