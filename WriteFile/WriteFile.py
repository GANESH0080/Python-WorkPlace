# Open / Create doc file
# W is used for create field
# Plus sign used for it will create a file if it does not exist in library
m = open("PythonFile.doc","w+")
m.write("Ganesh Salunkhe")

# Append added same text in file on every run
# Address file created without extension
m = open("Address","a+")
m.write("Kalamboli, Navi Mumbai")