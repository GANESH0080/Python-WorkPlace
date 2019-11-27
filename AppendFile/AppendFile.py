# Open file in append mode.
# If file does not exist, it creates a new file.
fis = open("appndedfiles.txt","a")

# Using for loop print 1 to 10 numbers in file
for i in range (10):
    fis.write("numbers are : %d\r\n" % (i+1))

    #Closing the file
fis.close()

# Truncate the file thw file which has already created
# This Mode Opens file for writing.
# If file does not exist, it creates a new file.
# If file exists it truncates the file.
fis = open("appndedfiles.txt", "w")
