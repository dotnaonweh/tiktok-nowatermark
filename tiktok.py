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
    'Referer': 'https://savetiktok.cc/en/download?url=',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}

url = input("Link Video => ")
response = requests.get('https://savetiktok.cc/en/download?url='+url, headers=headers).text
rex = re.findall('<option value="(.*?)"', response)[0]
video_url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|)+', rex)[0].replace("&amp;", "&")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
    'Alt-Used': 'savetiktok.cc',
    'Connection': 'keep-alive',
    'Referer': 'https://savetiktok.cc/en/download?url=',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}

name = random.randrange(0, 1000)
res_video = requests.get(video_url, headers=headers)
with open("Result/tiktok-"+str(name)+".mp4", 'wb') as fl:
    fl.write(res_video.content)
    fl.close()
print("Result/tiktok-"+str(name)+".mp4")
print("Done, Check folder Result")
