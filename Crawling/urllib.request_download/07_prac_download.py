import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://ssl.pstatic.net/tveta/libs/1276/1276699/e62597a4aefc4587e9c3_20200212145541194.jpg"
videoUrl = "https://tvetamovie.pstatic.net/libs/1274/1274962/7d0eca8001c112298efd_20191129185648851.mp4-pBASE-v0-f95905-20191129185731318.mp4"

savePath1 = "E://img.jpg"
savePath2 = "E://video.mp4"

file1 = req.urlopen(imgUrl).read()
file2 = req.urlopen(videoUrl).read()

with open(savePath1,'wb') as f:
    f.write(file1)

with open(savePath2,'wb') as f2:
    f2.write(file2)
