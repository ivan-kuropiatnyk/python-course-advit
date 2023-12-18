from urllib import request, parse
import sys

myUrl = "https://www.google.com/search?"

value = {'q': 'ANDRESA Soft'}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'

try:
    mydata = parse.urlencode(value)
    print(mydata)
    myUrl = myUrl + mydata
    req = request.Request(myUrl, headers=myheader)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)
except Exception:
    print("Error during web request!")
    print(sys.exc_info()[1])
