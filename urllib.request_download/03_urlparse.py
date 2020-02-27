import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.google.com/"

mem = req.urlopen(url)

print("geturl : ", mem.geturl())
print("status : ", mem.status)
print("headers : ",mem.getheaders())
print("info : ", mem.info())
#print("read : ", mem.read().decode("utf-8")) # 문자열이 크기때문에 에러
print(urlparse("https://www.google.com/"))
