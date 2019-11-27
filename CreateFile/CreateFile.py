# Create an file on specific location
# This Mode Opens file for writing.
# If file does not exist, it creates a new file.
# If file exists it truncates the file.
f= open("D:\python999.txt","w+")

# Created file in same project
M= open("python999.txt","w+")



# We declared the variable f to open a file named textfile.txt. Open takes 2 arguments,
# the file that we want to open and
# a string that represents the kinds of permission or operation we want to do on the file

# Here we used "w" letter in our argument, which indicates
# write and the plus sign that means it will create a file if it does not exist in library

# The available option beside "w" are "r" for read and "a" for append and plus sign means
# if it is not there then create it