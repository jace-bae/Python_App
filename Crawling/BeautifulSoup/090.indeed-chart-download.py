from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%86%A0%EB%A1%A0%ED%86%A0"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,'html.parser')

list = soup.find_all(class_='review_content')
print(list)
# for i in list:
#     print(i.attrs['href'])
