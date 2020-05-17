#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 20:18
# @Author  : Ian_Zhou
# @Email   : zhoujian_2008@msn.com
# @File    : lesson3_repositories_message_send_to_phone_by_pushover.py
# @Function:
# @Software: PyCharm

# https://api.pushover.net/1/messages.json?token=aros1qr4ztmjqmrruztjvpfr74zu3g&user=u1ujwu3beabx845g3ymqhka4bzvsab&message=hi&url=www.github.com

# https://api.github.com/search/repositories?q=topic:crawler+language:python+created:2020-05-15

import requests
from datetime import datetime


def get_repo():
    # api = 'https://api.github.com/search/repositories?q=topic:crawler+language:python+created:' + str(datetime.now()).split()[0]
    api = 'https://api.github.com/search/repositories?q=topic:crawler+language:python+created:' + "2018-05-16"
    repo_items = requests.get(api).json()['items']
    return repo_items


def send_message(repo_items):
    for item in repo_items:
        name = item['name']
        description = item['description']
        url = item['html_url']
        user = 'u1ujwu3beabx845g3ymqhka4bzvsab'
        token = 'aros1qr4ztmjqmrruztjvpfr74zu3g'
        post_message = f"https://api.pushover.net/1/messages.json?token={token}&user={user}&message={description}&url={url}&title={name}r"
        requests.post(post_message)
        print('Done')


def main():
    repo = get_repo()
    send_message(repo)


if __name__ == '__main__':
    main()
