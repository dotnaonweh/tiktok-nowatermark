import requests
import re
import random
import os

try:
    os.mkdir('Result')
except:
    pass

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
    'Alt-Used': 'savetiktok.cc',
    'Connection': 'keep-alive',
    'Referer': 'https://savetiktok.cc/en/download?url=https%3A%2F%2Fwww.tiktok.com%2F%40ni94%2Fvideo%2F69996',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}
filename = random.randrange(0, 1000)
url = input("Link Video => ")
response = requests.get('https://savetiktok.cc/en/download?url='+url, headers=headers).text
rex = re.findall('<option value="(.*?)"', response)[0]
video_url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|)+', rex)[0].replace("&amp;", "&")
res_video = requests.get(video_url, headers=headers)
with open("Result/tiktok-"+str(filename)+".mp4", 'wb') as fl:
    fl.write(res_video.content)
    fl.close()
print("DOWNLOAD DONE, CHECK FOLDER Result")
