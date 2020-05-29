#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 20:18
# @Author  : Ian_Zhou
# @Email   : zhoujian_2008@msn.com
# @File    : lesson4_weibo.py
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
    sel = 'span > span.line.S_line1 > span > em:nth-child(2)'
    driver = start_chrome()
    driver.get(url)
    time.sleep(10)
    elems = driver.find_elements_by_css_selector(sel)
    return [int(el.text) for el in elems[1:]]


def main():
    while True:
        url = 'https://weibo.com/5902696506/J3KWmqkQg?ref=feedsdk&type=comment#_rnd1590585251530'
        info = find_info(url)
        rep, comm, like = info
        if rep > 7000:
            print(f'转发量已经为{rep}')
            break
        else:
            print('Not happen!')
        time.sleep(1200)
    print('DONE!')


if __name__ == '__main__':
    main()
