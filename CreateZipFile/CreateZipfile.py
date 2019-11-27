import os
import shutil
from os import path
from zipfile import ZipFile
from os import path
from shutil import make_archive


file = open("File1.txt","w+")
file.write("Ganesh Salunkhe")

file.close()
fileread = open("File1.txt","r")
read = fileread.read()
print(read)
fileread.close()

if path.exists("File1.txt"):
    src = path.realpath("File1.txt")

root_dir,tail = path.split(src)
print(root_dir)
print(tail)

shutil.make_archive("File1 archive","zip",root_dir)

