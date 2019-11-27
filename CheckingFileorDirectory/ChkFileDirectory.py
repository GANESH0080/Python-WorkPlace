import os.path
from os import path

# Created an file
w = open("file.txt","w+")
m = open("D:\PythonWorkPlace\samplefile.txt","w+")

# Checking file exist in directory or not
print("file exist:" + str(path.exists("guru99.txt")))
print("file exists:" + str(path.exists("file.txt")))
print("Directory exists:" + str(path.exists("D:\PythonWorkPlace")))
print("Directory exists:" + str(path.exists("samplefile.txt")))