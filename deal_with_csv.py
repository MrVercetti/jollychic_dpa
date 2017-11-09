# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pandas as pd

df = pd.read_csv('jollychic test.csv')

print df

df_dpa = pd.DataFrame(
    columns=[u'id', u'title', u'description', u'availability', u'condition', u'price', u'link', u'image_link', u'brand',
             u'additional_image_link', u'age_group', u'color', u'gender', u'item_group_id', u'google_product_category',
             u'material',
             u'pattern', u'product_type', u'sale_price', u'sale_price_effective_date', u'shipping', u'shipping_weight',
             u'size',
             u'custom_label_0', u'custom_label_1', u'custom_label_2', u'custom_label_3', u'custom_label_4'])
