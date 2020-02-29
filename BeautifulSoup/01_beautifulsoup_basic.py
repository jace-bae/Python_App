from bs4 import BeautifulSoup
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
    <h1>Python Study BeautifulSoup</h1>
    <p>Tag Selector</p>
    <p>CSS Selector</p>

    <h2>Tag Selector - list</h2>
    <ul>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
    </ul>

    <div id="css_sel">
        <h2>CSS Selector</h2>
        <ul class="lecs">
            <li>python_basic</li>
            <li>python_crawling</li>
            <li>python_selenium</li>
            <li>java programming</li>
        </ul>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html,'html.parser')

# 태그 선택자
h1 = soup.h1
print(h1.string)
p1 = soup.p
print(p1.string)
p2 = p1.next_sibling.next_sibling
print(p2.string)
p3 = p2.previous_sibling.previous_sibling
print(p3.string)
print()

link = soup.find_all('a')
for li in link:
    href = li.attrs['href']
    txt = li.string
    print(txt,':',href)
print()

# CSS 선택자
list = soup.select('div#css_sel>ul.lecs>li')
for list_li in list:
    print(list_li.string)

h2 = soup.select_one('div#css_sel > h2')
print(h2.string)
