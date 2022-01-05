import requests
import re
import random

def tiktok(target):
    try:
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
        filename = random.randrange(0, 1000)
        if 'tiktok.com' not in target:
            print("Link Error")
        # new tiktok mobile link vt.tiktok.com change to tiktok.com/t
        elif 'tiktok.com/t/':
            response = requests.get(target).text
            regex = re.findall('content="(.*?)"', response)[-1].replace("&amp;", "&")
            response1 = requests.get('https://savetiktok.cc/en/download?url='+regex, headers=headers).text
            regex = re.findall('<option value="(.*?)"', response1)[0]
            video_url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|)+', regex)[0].replace("&amp;", "&")
            res_video = requests.get(video_url, headers=headers)
            with open("Result/tiktok-"+str(filename)+".mp4", 'wb') as fl:
                fl.write(res_video.content)
            print("Download done, check folder Result")
        else:
            response = requests.get('https://savetiktok.cc/en/download?url='+target, headers=headers).text
            regex = re.findall('<option value="(.*?)"', response)[0]
            video_url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|)+', regex)[0].replace("&amp;", "&")
            res_video = requests.get(video_url, headers=headers)
            with open("Result/tiktok-"+str(filename)+".mp4", 'wb') as fl:
                fl.write(res_video.content)
            print("Download done, check folder Result")
    except:
        pass

x = input("Link nya > ")
print('Wait....')
tiktok(x)
