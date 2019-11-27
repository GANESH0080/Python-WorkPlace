import urllib.request

# open a connection to a URL using urllib2
weburl = urllib.request.urlopen('http://test.cogitate.us/MH.Test/')

#get the result code and print it
print("Get Response:" ,str(weburl.getcode()))

# Call the read function on the webURL variable
#  Read the entire content of the URL into a variable called data
data = weburl.read()

print(data)