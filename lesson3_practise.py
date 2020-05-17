#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 20:18
# @Author  : Ian_Zhou
# @Email   : zhoujian_2008@msn.com
# @File    : lesson3_practise.py
# @Function: 推送 github 上最近的优秀的库到手机上
# @Software: PyCharm

# https://api.pushover.net/1/messages.json?token=aros1qr4ztmjqmrruztjvpfr74zu3g&user=u1ujwu3beabx845g3ymqhka4bzvsab&message=hi&url=www.github.com

# https://api.github.com/search/repositories?q=topic:crawler+language:python+created:2020-05-15

import requests
from datetime import datetime, timedelta
import time


def get_repo():
    """获取 github 上项目"""
    api = 'https://api.github.com/search/repositories?q='
    # api = 'https://api.github.com/search/repositories?q=topic:crawler+language:python+created:' + "2018-05-16"
    search_info = "topic:blockchain+language:python+stars:>=200+created:>"
    search_time = str(datetime.now() + timedelta(days=-7)).split()[0]
    api_url = api + search_info + search_time
    repo_items = requests.get(api_url).json()['items']
    return repo_items


def send_message(repo_items):
    """通过 pushover 发送"""
    if repo_items:
        for item in repo_items:
            name = item['name']
            description = item['description']
            url = item['html_url']
            user = 'u1ujwu3beabx845g3ymqhka4bzvsab'
            token = 'aros1qr4ztmjqmrruztjvpfr74zu3g'
            post_message = f"https://api.pushover.net/1/messages.json?token={token}&user={user}&message={description}&url={url}&title={name}r"
            requests.post(post_message)
            print('Done')
    else:
        print("There is no new repositories!")


def main():
    """
    主函数
    """
    repo = get_repo()
    while True:
        send_message(repo)
        time.sleep(600)


if __name__ == '__main__':
    main()
