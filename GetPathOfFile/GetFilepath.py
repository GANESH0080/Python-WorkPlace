import os
import shutil
from os import path

# Created file 
w = open("getPathFileone.txt", "w+")
w.close()

# Store the file path in the variable src If txt file exist
if(path.exists("getPathFileone.txt")):

 src = path.realpath("getPathFileone.txt");

# Use src variable to split the path & filename
haid, tail = path.split(src)
print ("Path :", haid)
print ("File :", tail)