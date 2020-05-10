#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 16:12
# @Author  : Ian_Zhou
# @Email   : zhoujian_2008@msn.com
# @File    : lesson1_practise.py
# @Function:
# @Software: PyCharm

import requests
import webbrowser
import time

api = "http://api.github.com/users/kennethreitz/starred"
starred_list = requests.get(api).json()
starred = []
for i in starred_list:
    starred.append(i['id'])

while True:
    info = requests.get(api).json()
    for i in info:
        if i['id'] not in starred:
            starred.append(i['id'])
            repo_name = i['name']
            owner = i['owner']['login']
            web_page = 'https://github.com/' + owner + "/" + repo_name
            webbrowser.open(web_page)
    time.sleep(600)
