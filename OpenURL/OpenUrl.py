import urllib.request

# Created an string weburl and enter the request for opening the URL
weburl = urllib.request.urlopen('https://www.guru99.com/')

# Printing an response code for verifying request was successfull or not
print("Result code : " +str(weburl.getcode()))
