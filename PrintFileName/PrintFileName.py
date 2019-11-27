# Created the file
fo = open("pythonpractive.txt","w+")

# Created variable and store the fiel name in variable
name = fo.name

# Printing the filename
print("FileName is :" +name)

# Write content into string
fo.write("Ganesh Salunkhe")

# Closing the file
fo.close()

# This will terminate the entered string , This will work only when user closed the file above
fo = open("pythonpractive.txt","w+")
fo.close()

fo = open("pythonpractive.txt","w+")
for i in range(5):
    fo.write("Numbers are : %d\r\n" % (i+1))
