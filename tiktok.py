import requests
import re
import random
import os
import sys
import time


def tiktok(target):
    headers = {
        'authority': 'api.app.downtik.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://downtik.com',
        'referer': 'https://downtik.com/',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0',
    }

    data = {
        'url': target,
        'lang': 'id',
    }
    filename = random.randrange(0, 1000)
    if 'tiktok.com' not in data['url']:
        print("Link Error")
    else:
        response = requests.post(
            'https://api.app.downtik.com/a.php', headers=headers, data=data).text
        regex = re.findall('<a href="(.*?)"', response)[0]
        res_video = requests.get(regex, headers=headers)
        with open("Result/tiktok-"+str(filename)+".mp4", 'wb') as fl:
            fl.write(res_video.content)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("                  Tiktok No Watermark Downloader")
            print("")
            animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%",
                         "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]
            for i in range(len(animation)):
                time.sleep(0.5)
                sys.stdout.write("\r[+] Downloading... " +
                                 animation[i % len(animation)])
                sys.stdout.flush()
            print("\n[*] Download done, check folder Result.")


x = input("[*] Link Video > ")
tiktok(x)
