import os
import shutil
from os import path


w = open("CreateCopyFile.txt", "w+")
w.write("Ganesh Salunkhe")
w.close()

if path.exists("CreateCopyFile.txt"):

    src = path.realpath("CreateCopyFile.txt")
print(src)
haid, tail = path.split(src)
print ("Directory path : " , haid)
print ("Filename : ", tail)


dst = src + ".bak"
print(dst)
shutil.copy(src , dst)
# Copystat function give the permission to .bak file for modification
# shutil.copystat(src , dst)