# Open / Create doc file
# W is used for create field
# Plus sign used for it will create a file if it does not exist in library
m = open("PythonFile.doc","w+")
m.write("Ganesh Salunkhe")
m.write("\n")

for i in range(10):
     m.write("This is line %d\r\n" % (i+1))

m.close()