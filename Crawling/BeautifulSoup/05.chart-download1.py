# naver 금융 - list

from bs4 import BeautifulSoup
import urllib.request as req

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://finance.naver.com/"
res = req.urlopen(url).read().decode(req.urlopen(url).headers.get_content_charset())
soup = BeautifulSoup(res,"html.parser")

# print(soup)

top = soup.select("ul.list_rank > li")
# print(top)

for i,e in enumerate(top,1): #시작 인덱스를 1로
    print(i,":",e.find("a").string)
