# Created an File
file = open("ReadFile.txt" ,"w+")

# Enter string into the file and stored into variable
file.write("Ganesh Salunkhe")

# Open the for for reading
file = open("ReadFile.txt" ,"r")

# Reading the file and store file date into variable
re= file.read()

# Printing file data
print(re)
