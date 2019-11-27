# Created an File
file = open("ReadFileOne.txt" ,"w+")

# Enter string into the file and stored into variable
te = file.write("Ganesh Salunkhe")

#Printing the string without read
print(te)

# Open the for for reading
r = open("ReadFile.txt" ,"r")

# Reading the file and store file date into variable
re= r.read()

# Printing file data
print(re)
