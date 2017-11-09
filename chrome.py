#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from selenium import webdriver

url = 'https://www.jollychic.com/womens-leggings-c42'

driver = webdriver.Chrome()
# driver.maximize_window()
# driver = webdriver.PhantomJS()
driver.get(url)

with open("hehe.html", 'w') as f:
    f.write(driver.page_source.encode('utf-8'))
