import os
import shutil
from os import path
from zipfile import ZipFile
from os import path
from shutil import make_archive

w = open("fileone.txt","w+")
w.close()

w = open("filey.txt","w+")
w.close()
w = open("filex.txt","w+")
w.close()

if path.exists("fileone.txt"):
    sr = path.realpath("fileone.txt")
haid, tail = path.split(sr)
print("path : ", haid)
print("File : " , tail)

shutil.make_archive("File1 archive","zip",haid)

with ZipFile("File1 archive.zip","w") as newzip:
    newzip.write("filey.txt")
    newzip.write("filex.txt")
    # not added in Zip file because you are trying to create file in runtime
   # newzip.write("filexyz.txt")
   # newzip.write("fileabc.txt","w+")