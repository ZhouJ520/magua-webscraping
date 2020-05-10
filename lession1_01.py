#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 15:44
# @Author  : Ian_Zhou
# @Email   : zhoujian_2008@msn.com
# @File    : lession1_01.py
# @Function:
# @Software: PyCharm

# api https://api.github.com/repos/channelcat/sanic
# web_page https://github.com/channelcat/sanic

import requests
import webbrowser
import time

api = "https://api.github.com/repos/channelcat/sanic"
repo_dicts = requests.get(api).json()
last_update = None
current_update = repo_dicts['updated_at']
web_page = "https://github.com/channelcat/sanic"

while True:
    if not last_update:
        last_update = current_update
        print("It's not updated now!")
    if last_update < current_update:
        webbrowser.open(web_page)
    time.sleep(600)