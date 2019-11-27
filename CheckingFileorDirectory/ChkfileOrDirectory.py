import os.path
from os import path

# Created an file
w = open("fileone.txt","w+")

# Checking file or directory
print("Is File:" + str(path.isfile("guru99.txt")))
print("Is File:" + str(path.isfile("fileone.txt")))
print("Directory exists:" + str(path.isfile("D:\PythonWorkPlace")))

print ("----------------------------------------")

# Checking file or directory
print("Is File:" + str(path.isdir("guru99.txt")))
print("Is File:" + str(path.isdir("fileone.txt")))
print("Directory exists:" + str(path.isdir("D:\PythonWorkPlace")))