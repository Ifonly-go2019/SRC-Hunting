# coding: UTF-8
# author: M0nk3y
# 功能实现：爬取所有学校网站的主站
# Data：2020/04/21
# 根据 http://www.hao123.com/edu  写一个爬虫，爬取所有大学的官方网站
import requests
import bs4
import time
import os

logo = """
___________________   ____ ___          ________                        .__                 ________                      .__
\_   _____/\______ \ |    |   \         \______ \   ____   _____ _____  |__| ____           \______ \____________ __  _  _|  |   ___________
 |    __)_  |    |  \|    |   /  ______  |    |  \ /  _ \ /     \__  \ |  |/    \   ______  |    |  \_  __ \__  \ \/ \/ /  | _/ __ \_  __ 
 |        \ |    `   \    |  /  /_____/  |    `   (  <_> )  Y Y  \/ __ \|  |   |  \ /_____/  |    `   \  | \// __ \     /|  |_\  ___/|  | \/
/_______  //_______  /______/           /_______  /\____/|__|_|  (____  /__|___|  /         /_______  /__|  (____  /\/\_/ |____/\___  >__|
        \/         \/                           \/             \/     \/        \/                  \/           \/                 \/
"""
print(logo)
print("[+]------------Loading----------[+]")
time.sleep(1)
url = 'http://www.hao123.com/edu'
r = requests.get(url)
rSoup = bs4.BeautifulSoup(r.text, 'html.parser')
for i in range(32):
    for k in rSoup.find_all('a'):
        if 'edu' not in k['href']:
            continue
        if 'gaokao' in k['href']:
            continue
        if 'htm' not in k['href']:
            continue
        else:
            try:
                a = k['href']
                r = requests.get(a)
                rSoup = bs4.BeautifulSoup(r.text, 'html.parser')
                for g in rSoup.find_all('a'):
                    if 'baidu' in g['href']:
                        continue
                    if 'sina' in g['href']:
                        continue
                    if 'hao123' in g['href']:
                        continue
                    if 'javascript' in g['href']:
                        continue
                    else:
                        a = g['href']
                        print(a)
                        file_handle = open('result.txt', 'a')
                        file_handle.write(a)
                        file_handle.write('\n')
                        file_handle.close()
            except KeyError:
                pass

print("[+]-------------ALL Done！------------[+]")
