s= open("SampleFile.txt","r")
if s.mode == 'r':
    contents = s.read()
    print(contents)