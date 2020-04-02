from bs4 import BeautifulSoup
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
<h1>python BeautifulSoup study</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
"""

soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify()) 이쁘게 정렬해서 나열

h1 = soup.html.body.h1
print(h1)
print(h1.string)
print(">>>>>>")

p1 = soup.html.body.p # 이경우 첫번째 p태그를 가지고옴
print(p1)
print(">>>>>>")

p2 = p1.next_sibling.next_sibling # 두번 쓴 이유는 html안에 첫번쨰 p태그 안에 \n이 생략되었기 때문
print(p2.string)
print(">>>>>>")

p3 = p1.previous_sibling.previous_sibling
print(p3)
