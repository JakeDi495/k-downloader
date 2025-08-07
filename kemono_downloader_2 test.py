
# -*- coding: cp1251 -*-

import time
import json
from urllib import response
import requests
from bs4 import BeautifulSoup


main_link = "https://kemono.cr/patreon/user/71053882"
main_link = main_link.split("/")


link_post = "https://kemono.cr/patreon/user/71053882/post/126065763"
link_post = link_post.split("/")

link_pict = f"https://kemono.cr/api/v1/patreon/user/{main_link[-1]}/post/{link_post[-1]}"

#
response = requests.get(link_pict).text
link_file_pic = json.loads(response)

# #print(f"https://n1.kemono.cr/data{link_file_pic["post"]["attachments"][0]["path"]}")

# #print(link_file_pic["post"]["attachments"][0])


for key in link_file_pic["previews"]:
    
    pic_bytes = requests.get(f"{key["server"]}/data{key["path"]}").content
    with open(f"{key["name"]}", 'wb') as file:
        file.write(pic_bytes)
    print(f"{key["server"]}/data{key["path"]}")



# link = "https://n2.kemono.cr/data/b0/99/b0996ca0f2cde0d5ce97dd7deba51133f2aa4c8ba69cdd151fa951a9cbd554de.pdf?f=Dont+Be+An+Ass+1-133.pdf"
# pic_bytes = requests.get(link).content
# with open(f"123.pdf", 'wb') as file:
#     file.write(pic_bytes)
# print(f"123.pdf")








