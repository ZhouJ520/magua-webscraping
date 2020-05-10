#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 16:23
# @Author  : Ian_Zhou
# @Email   : zhoujian_2008@msn.com
# @File    : lesson2_01.py
# @Function:
# @Software: PyCharm

# https://api.github.com/search/repositories?q=django
# https://api.github.com/search/repositories?q=topic:django


import requests
import webbrowser


def get_names():
    names = input("Separate each name with Space:")
    return names.split()


def check_repos(names):
    repo_api = 'https://api.github.com/search/repositories?q='
    ecosys_api = 'https://api.github.com/search/repositories?q=topic:'
    for name in names:
        repo_info = requests.get(repo_api + name).json()['items'][0]
        stars = repo_info['stargazers_count']
        forks = repo_info['forks_count']
        ecosys_info = requests.get(ecosys_api + name).json()['total_count']
        print(name)
        print('Stars:', stars)
        print('Forks:', forks)
        print('Ecosys:', ecosys_info)
        print("---------------")


names = get_names()
check_repos(names)