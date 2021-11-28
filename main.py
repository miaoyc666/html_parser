#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : main.py
Author       : miaoyc
Create date  : 2021/11/14 2:34 上午
Description  :
"""

from bs4 import BeautifulSoup
from bs4.element import NavigableString


def get_children(tag):
    return [child for child in tag.children if not isinstance(child, NavigableString)]


def get_url_title(title_tag):
    child = get_children(title_tag)[0]
    href = child["href"]
    url = "https://testtesttest.com{0}".format(href)
    return url, child["title"]


def get_magnet(magnet_tag):
    child = get_children(magnet_tag)[1]
    magnet = child["href"]
    return magnet


def parse_html(file_path):
    html_doc = open(file_path)
    soup = BeautifulSoup(html_doc, 'html.parser')
    tr_list = soup.find_all(name='tr', attrs={"class": "default"})
    res_list = []
    for tr in tr_list:
        children = get_children(tr)
        title_tag = children[1]
        magnet_tag = children[2]
        size_tag = children[3]
        time_tag = children[4]
        #
        url, title = get_url_title(title_tag)
        magnet = get_magnet(magnet_tag)
        size = size_tag.string
        create_time = time_tag.string
        s_id = url.split("=")[-1]
        res_list.append((s_id, url, title, magnet, size, create_time))
    return res_list


if __name__ == '__main__':
    for index in range(1, 3):
        url_ = "https://testesttestest.com?p={0}".format(index)
        file_name = time.strftime("%Y-%m-%d-%H-%M-%S.html", time.localtime(time.time()))
        file_path_ = '/home/miaoyc/test_path/html/{0}'.format(file_name)
        os.system("wget {0} -O {1}".format(url_, file_path_))
        parse_html(file_path_)
        dat_list = parse_html(file_path_)
        print(dat_list)

