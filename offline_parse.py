#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from bs4 import BeautifulSoup
import pandas as pd
import re

with open('hehe.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')

    # 获取商品列表
    product_list = soup.select('#J-pro-list > li')

    for product in product_list:
        # fb_id
        fb_id = product.attrs['data-gid']
        # print fb_id

        # fb_title
        fb_title = product.select('a > h5')[0].get_text()
        # print fb_title

        # fb_price
        try:
            fb_price = product.find_all('span')[1].get_text()
            fb_price = re.findall(r'\$(.*)', fb_price)[0]+' USD'
        except Exception:
            fb_price = ''
        # print fb_price

        # fb_link
        fb_link = product.select('a')[0].attrs['href']
        # print fb_link

        # fb_image_link
        fb_image_link = product.select('img.J-lazy-load.firstImg')[0].attrs['data-original'].split('_')[0]
        # print fb_image_link

        # add_wish
        add_wish = product.find_all('span')[0].get_text()
        # print add_wish

        # 数据打包
        data = {
            'id': fb_id,
            'title': fb_title,
            'price': fb_price,
            'link': fb_link,
            'image_link': fb_image_link,
            'add_wish': add_wish,
        }
        print data
        df_data = pd.DataFrame(data, index=[0])
        # print df_data

"""
#J-pro-list > li:nth-child(1) > div.pro_list_imgbox.categoryTwo-imgbox > a > img.J-lazy-load.firstImg

"""
