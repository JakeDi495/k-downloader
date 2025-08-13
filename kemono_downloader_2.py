
# -*- coding: cp1251 -*-

import time
import json
from urllib import response
import requests
from bs4 import BeautifulSoup
import fake_useragent


#link patreon artist or id
main_link = "https://kemono.cr/patreon/user/71053882"
main_link = main_link.split("/")

num_bottom = 115
num_top = 9999999

num = 0

user = fake_useragent.UserAgent().random
header = {"user-agent": user}


#page inspection
for a in range(0, 300, 50):
    

    link_req = f"https://kemono.cr/api/v1/patreon/user/{main_link[-1]}/posts?o={a}"

    #request page json file
    response = requests.get(link_req, headers = header).text
    link_file = json.loads(response)

    # print(link_file, "\n", "\n", "\n")

    # #stop page inspection
    if response.count("error") > 0:
        break



    #inspection page json file for find post id
    for post in link_file:
        
         #################################
         #request post json file
        link_data_pict = f"https://kemono.cr/api/v1/patreon/user/{main_link[-1]}/post/{post["id"]}"

        response_post = requests.get(link_data_pict, headers = header).text
        link_file_pic = json.loads(response_post)

        if response_post.count("SSLError") > 0:
            continue

        #inspection post json file for find picture/file link
        for pic in link_file_pic["previews"]:
            
            num+=1

            if num < num_bottom or num > num_top:
                continue

            #get picture/file link for download
            pic_bytes = requests.get(f"{pic["server"]}/data{pic["path"]}", headers = header).content
            
            # download picture/file, name = [post name], [picture name] 

            with open(f"download/{post["title"]}, {pic["name"]}", 'wb') as file:
                file.write(pic_bytes)

            print(num, f"{post["title"]}, {pic["name"]}", "  -  ", f"{pic["server"]}/data{pic["path"]}")


        ############################################
        
        
       

#soup = BeautifulSoup(response, "lxml")

#blocks = soup.find("div", class_="header")

# for i in elem:
#     pic = i.get_attribute('href')
#     print("!!!!!!!!!", pic, "\n")


#     image_bytes = requests.get(pic).content

    
#     with open(f"{n}.jpg", 'wb') as file:
#         file.write(image_bytes)
#     n+=1










