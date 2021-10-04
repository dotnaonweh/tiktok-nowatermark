import requests
import re
import html
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

name = random.randrange(0,1000)
url = input("Link Video => ")
req_url = requests.get('https://savetiktok.cc/en/download?url='+url, headers=headers).text
rex = re.findall('<option value="(.*?)"', req_url)
rep = rex[0]
rx = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|)+', rep)
result = html.unescape(rx)
x = result[0]
replacing = x.replace("&amp;", "&")
url = replacing

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

name = random.randrange(0,1000)
req_video = requests.get(url, headers=headers)
with open("Result/tiktok-"+str(name)+".mp4", 'wb') as fl:
    fl.write(req_video.content)
    fl.close()
print("\nDone, Check folder Result")
# import requests
# import re
# import html
# import json
# import random
# import os
# from bs4 import BeautifulSoup

# try:
#     os.system("cls")
# except:
#     pass

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
#     'Alt-Used': 'savetiktok.cc',
#     'Connection': 'keep-alive',
#     'Referer': 'https://savetiktok.cc/en/download?url=',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
# }

# url = input("Link Video => ")
# req_url = requests.get('https://savetiktok.cc/en/download?url='+url, headers=headers).text
# rex = re.findall('<option value="(.*?)"', req_url)
# for i in rex:
#     rp = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|)+', i)
#     result = html.unescape(rp[0])
#     r2 = result.split("tiktokv.com'")[0]
#     print("=>", r2)

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
#     'Alt-Used': 'savetiktok.cc',
#     'Connection': 'keep-alive',
#     'Referer': 'https://savetiktok.cc/en/download?url=',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
# }

# name = random.randrange(0,1000)
# url = input("Link nya = > ")
# req_video = requests.get(url, headers=headers)
# with open("S No WM/tiktok-"+str(name)+".mp4", 'wb') as fl:
#     fl.write(req_video.content)
#     fl.close()
# print("\nBERHASIL KE DOWNLOAD A")