import os

w = open("RenameFilef.txt","w+")

w.write("Ganesh Salunkhe")

w.close()

m= open("RenameFilef.txt","r")

str = m.read()

print("Your string is : ",str)

m.close()


os.rename("RenameFilef.txt","career.guru99.txt")


