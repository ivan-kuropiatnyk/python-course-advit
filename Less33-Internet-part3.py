from urllib import request
import sys

myUrl = "https://adv400.tripod.com/kartinka.jpg"
myfile = "D:\\kartinka.jpg"

try:
    print("Start downloading file from:" + myUrl)
    request.urlretrieve(myUrl, myfile)
except Exception:
    print("Ahtung!")
    print(sys.exc_info())
    exit()

print("File Downloaded to:" + myfile)
