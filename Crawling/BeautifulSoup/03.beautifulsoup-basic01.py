# 태그선택자 사용

from bs4 import BeautifulSoup
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html,'html.parser')

links = soup.find_all("a") #태그를 한번에 담아라

a = soup.find_all("a", string="google")
print(a)

b = soup.find_all("a", limit = 3)
print(b)

for a in links:
    href = a.attrs['href'] #key 값을 입력 딕셔너리 형태로 반환(키와 밸류)
    txt = a.string
    print(txt, ' : ', href)
