import xml.dom.minidom

# Reading the XML for parsing
doc = xml.dom.minidom.parse("firstXML.xml");

# Print the Nodename of XML doc, Entire XML doc is document Node
print(doc.nodeName)

# Printing the Tagname of FirstChild
print(doc.firstChild.tagName)

# Finding the Nodes which names has "firstname" and store into the variable
fnameTags = doc.getElementsByTagName("firstname")
# Printing the length of elements which names has ""firstname"
print("FirstName Tags are :" ,fnameTags.length)



# Finding the Nodes which names has "Lastname" and store into the variable
lnameTags = doc.getElementsByTagName("LastName")
# Printing the length of elements which names has ""lname"
print("LastName Tags are :" ,lnameTags.length)

# For loop for getting the FirstNames in the XML
for skill in fnameTags:
    # Printing the First names
 print("FirstName Values are :" ,skill.firstChild.data)

print("-----------******************-------------------")

# For loop for getting the LastNames in the XML
for skill in lnameTags:
    # Printing the Last names
     print("LastName Values are :", skill.firstChild.data)