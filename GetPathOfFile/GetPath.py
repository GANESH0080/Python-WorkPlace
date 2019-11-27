import os
import shutil
from os import path
# Store the file path in the variable src If txt file exist
if(path.exists("D:\PythonWorkPlace\samplefile.txt")):

 src = path.realpath("D:\PythonWorkPlace\samplefile.txt");

# Use src variable to split the path & filename
haid, tail = path.split(src)
print ("Path :", haid)
print ("File :", tail)