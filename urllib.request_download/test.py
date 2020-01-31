import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url1 = "https://ssl.pstatic.net/tveta/libs/1272/1272090/12ad93e4f6f3a1df7b5e_20200129134156474.jpg"
url2 = "https://tvetamovie.pstatic.net/libs/1272/1272084/4320db9c1b953d678e25_20200123114258431.wmv-pBASE-v0-f98042-20200123114750225.mp4"

savePath1 = "url1.jpg"
savePath2 = "url2.mp4"

file1 = dw.urlopen(url1).read()
with open(savePath1,'wb') as save1:
    save1.write(file1)

file2 = dw.urlopen(url2).read()
with open(savePath2, 'wb') as save2:
    save2.write(file2)

print("download success")
