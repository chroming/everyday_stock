# -*- coding:utf-8 -*-

import requests



def check_stock(sn):
    stock_response = requests.get('http://hq.sinajs.cn/list=%s' % sn)
    if stock_response:
        stock_text = stock_response.text
        stock_code_list = stock_text.split("\"")
        if len(stock_code_list) == 3:
            stock_code = stock_code_list[1]
            stock_fina_list = stock_code.split(",")
            if len(stock_fina_list) == 33:
                print stock_fina_list

# 上证
for shi in range(600000, 604000):
    shi = 'sh' + str(shi)
    check_stock(shi)

# 深证1
for szi in range(0, 2801):
    szi = 'sz' + str(sz).zfill(6)
    check_stock(szi)


for szj in range(300000, 3000517):
    szi = 'sz' + str(sz).zfill(6)
    check_stock(szi)