import requests
import re

url = "https://pic.sogou.com/pics?from=homeHotSearch&query=%E6%83%85%E4%BE%A3%E5%A4%B4%E5%83%8F"

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
          "Accept-Ranges":"bytes",
          "Access-Control-Allow-Credentials":"true",
          "Access-Control-Allow-Origin":"https://image.baidu.com",
          "Age":"197265"}

response = requests.get(url=url, headers=header)
response.encoding = "utf-8"
response = response.text
print(response)

img_url_list = re.findall('"oriPicUrl":"(.*?)"', response)

print(img_url_list)
count = 0
for i in img_url_list:
    count = count + 1
    print(count)
    img = requests.get(i)
    with open("./picture/图片%s.jpg" % count, "wb") as file:
        file.write(img)