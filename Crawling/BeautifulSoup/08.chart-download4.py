# 인프런
from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.inflearn.com/"

res = req.urlopen(url).read().decode(req.urlopen(url).headers.get_content_charset())
soup = BeautifulSoup(res,"html.parser")

recommand = soup.select("section.inf_slider relative_courses section background_grey courses_slide_tmpl")
print(recommand)
