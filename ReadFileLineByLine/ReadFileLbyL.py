# We declared the variable f to open a file named textfile.txt. Open takes 2 arguments, the file that we want to open
# and a string that represents the kinds of permission or operation we want to do on the file

s = open("pythonfileone.txt","w+")
# Using For loop we are printing / writing 1 to 10 numbers in file
for i in range(10):
    s.write("values are %d\r\n" %(i+1))
    # Closing the file
s.close()

#Open the file for reading
m = open("pythonfileone.txt","r")
# Stored read data in string
str = m.read()
# Print readed data
print(str)

# Write more data in file
s = open("pythonfileone.txt","w+")
for p in range(2):
    s.write("Appended lines are %d\r\n" %(p+1))
    # Closing the file
s.close()

# Open file for reading the data
n = open("pythonfileone.txt","r")
# Stored read data in string
stri = n.read()
# Print readed data
print(stri)
