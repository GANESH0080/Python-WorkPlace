fis = open("appnd.txt","a")
for i in range (10):
    fis.write("numbers are : %d\r\n" % (i+1))

fis = open("appnd.txt", "a")
for i in range(5):
        fis.write("Appended numbers are : %d\r\n" % (i + 1))