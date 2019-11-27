import os
import shutil
from os import path

# Store the file path in the variable src If txt file exist
if(path.exists("getPathFile.txt")):

 src = path.realpath("getPathFile.txt");

# Use src variable to split the path & filename
haid, tail = path.split(src)
print ("Path :", haid)
print ("File :", tail)