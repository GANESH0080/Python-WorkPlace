s = open("pythonfile.txt","w+")
s.write("Ganesh Salun")
s.close()
abx = open("pythonfile.txt", "r")
if abx.mode == "r":
  content = abx.read()
  print(content)