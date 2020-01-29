import sys
import io
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 원하는 이미지를 다운로드

imgURL = "http://post.phinf.naver.net/MjAxNzExMjZfMjM0/MDAxNTExNzA3ODY5MzI2.BMO-NoJUSlwN_-3y2qyEOPv6Wp9JIqcT5Qqj_C7i0Gsg.X-Jkr7_Dvn6J0VEudl5g-FwnShqTbVg2vES997CQaI4g.JPEG/Imr6VJjIVDTIBDPyyNx4Tkyt0yIo.jpg"
htmlURL = "http://google.com"

savePath1 = "G:/Python/python_auto/chapter1/test1.jpg"
savePath2 = "G:/Python/python_auto/chapter1/index.html"

urllib.request.urlretrieve(imgURL, savePath1)
urllib.request.urlretrieve(htmlURL, savePath2)

print("download pass")
