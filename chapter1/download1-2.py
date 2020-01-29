# 원하는 이미지를 하드디스크에 다운로드하는 방법

import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgURL = "http://post.phinf.naver.net/MjAxNzExMjZfMjM0/MDAxNTExNzA3ODY5MzI2.BMO-NoJUSlwN_-3y2qyEOPv6Wp9JIqcT5Qqj_C7i0Gsg.X-Jkr7_Dvn6J0VEudl5g-FwnShqTbVg2vES997CQaI4g.JPEG/Imr6VJjIVDTIBDPyyNx4Tkyt0yIo.jpg"
htmlURL = "http://google.com"

savePath1 = "G:/Python/python_auto/chapter1/test1.jpg"
savePath2 = "G:/Python/python_auto/chapter1/index.html"

f = dw.urlopen(imgURL).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb') # w: write , r : read, a : add
saveFile1.write(f)
saveFile1.close()

# with문 사용 - close가 자동
with open(savePath2,'wb') as saveFile2
    saveFile2.write(f2)

print("download pass")
