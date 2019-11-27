import xml.dom.minidom

# Reading the XML for parsing
doc = xml.dom.minidom.parse("SampleXML.xml");
newNode = doc.createElement("firstname")
newNode.setAttribute("name", "Mahape")
doc.firstChild.appendChild(newNode)
print(" ")
firstname = doc.getElementsByTagName("firstname")
print("Total %d FirstName Length :"% firstname.length)

for skill in firstname:
     print("FirstName Values are :", skill.getAttribute("name"))

file = open("SampleXML.xml","r")
str = file.read()
print(str)
file.close()
