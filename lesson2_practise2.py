#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 20:19
# @Author  : Ian_Zhou
# @Email   : zhoujian_2008@msn.com
# @File    : lesson2_practise2.py
# @Function:
# @Software: PyCharm

import requests

"""
api形式 /code?q=language:python+size:<200+repo:目录名
q参数：
    language:指定语言
    size:指定文件大小，如size:<200表示文件小于200KB
    repo:指定目录（必要参数）
示例：
    https://api.github.com/search/code?q=language:python+size:<200+repo:tensorflow/tensorflow
"""
get_code_api = "https://api.github.com/search/code?q="
get_repo_api = "https://api.github.com/search/repositories?q=language:python"


# 编写函数，实现在github某一目录下寻找code文件的功能
def get_code(language, size, repo):
    url = get_code_api + "language:" + language + "+size:" + size + "+repo:" + repo
    # 访问GitHub接口
    info = requests.get(url).json()
    if 'items' in info:
        for i in info['items']:
            print(i['html_url'])


# 编写函数，查找更新时间在last_week之后的项目
def get_project(last_week):
    # 访问GitHub接口
    info = requests.get(get_repo_api).json()
    for i in info['items']:
        created_time = i['created_at']
        if created_time > last_week:
            language = "python"
            size = "<200"
            # 从info数据中获取项目的目录
            repo = i['html_url'].replace("https://github.com/", "")
            # 传入三个限制条件，调用查找code文件的函数
            get_code(language, size, repo)


# 调用查找项目的函数，设定上个星期的时间
get_project("2018-03-3T00:00:00Z")
