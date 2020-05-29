#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 20:18
# @Author  : Ian_Zhou
# @Email   : zhoujian_2008@msn.com
# @File    : lesson4_practise.py
# @Function:  某关注微博量大于一定数量后进行推送
# @Software: PyCharm

from selenium import webdriver  # 打开浏览器库
import time


def start_chrome():
    """chrome程序开打器"""
    driver = webdriver.Chrome()
    driver.start_client()
    return driver


def find_info(url):
    # css selector
    sel = 'div.card-topic-a:nth-child(3) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)'
    driver = start_chrome()
    driver.get(url)
    time.sleep(10)
    elems = driver.find_element_by_css_selector(sel)
    return elems.text.replace('讨论', '')


def main():
    while True:
        url = 'https://s.weibo.com/weibo/%2523%25E5%25A5%25A5%25E6%2596%25AF%25E5%258D%25A1%2523&Refer=STopic_box'
        info = find_info(url)
        if info> '300万':
            print(f'讨论数量已经为{info}')
            break
        else:
            print('讨论数量不足300 万')
        time.sleep(1200)


if __name__ == '__main__':
    main()
