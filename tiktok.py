import requests
import json


def tiktok(target):
    headers = {
        'X-Rapidapi-Key': '3d204a970emshd8658b3f3e32d6dp138ebcjsn7a898b2a7b31',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
    }

    if 'tiktok.com' not in target:
        print("Link Error")
    else:
        response = requests.get(
            'https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index?url='+str(target), headers=headers)
        data = json.loads(response.text)
        videos = data['video'][0]
        filename = data['videoid'][0]
        res_video = requests.get(videos, headers=headers)
        with open("Result/"+str(filename)+".mp4", 'wb') as fl:
            fl.write(res_video.content)
            print("\n[*] Download done, check folder Result.")


x = input("[*] Link Video > ")
tiktok(x)
