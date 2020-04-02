#indeed scrapping
# what : qa tester
# where : toronto

from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url = "https://www.indeed.ca/jobs?q=qa+tester&l=Toronto%2C+ON"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,'html.parser')

# print(soup)
# list = soup.select("#resultsCol>div")
# for e in list:
#     if e.find("a"):
#         print(e)
#
# list = soup.find_all(class_="title")
#
# # for e in list:
# #     print(e.attrs['title'])
# # print('end')
# for i in list:
#     print(i.select_one(".title"))

list = soup.find_all(class_='title','sjcl')

for i in list:
    href = i.attrs['href'] #key 값을 입력
    txt = i.string
    print(txt, ' : ', href)
# for e in list:
#     href = e.attrs['title']
#     print(href)
