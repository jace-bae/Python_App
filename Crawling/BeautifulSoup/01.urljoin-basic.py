# pip install beautifulsoup4 로 먼저 설치 우선

from urllib.parse import urljoin

baseUrl = "http://test.com/html/a.html"
print(urljoin(baseUrl,"b.html")) # a.html을 제거하고 b로 치환 (절대경로 유지한 상태에서 변경)
print(urljoin(baseUrl,"sub/c.html"))
print(urljoin(baseUrl,"../index.html"))
