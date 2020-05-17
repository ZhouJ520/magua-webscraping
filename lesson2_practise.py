#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 19:11
# @Author  : Ian_Zhou
# @Email   : zhoujian_2008@msn.com
# @File    : lesson2_practise_private.py
# @Function:
# @Software: PyCharm

# https://api.github.com/search/repositories?q=languages:python

import requests
import time

api_info = "https://api.github.com/search/repositories?q=languages:"

cur_date = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime(time.time()))


def names():
    name = input("please input the language that you want to search:")
    return name


def search_projects(name, week):
    repo_info = requests.get(api_info + name).json()['items']
    try:
        for i in range(300):
            if repo_info[i]['size'] < 200 and repo_info[i]['created_at'][:10] > week:
                print(repo_info[i]['html_url'])
    except IndexError:
        pass


name = names()
week = input('please input the before week yyyy-mm-dd:')

print("The projects' size smaller than 200KB are below:")
search_projects(name, week)
