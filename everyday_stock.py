# -*- coding:utf-8 -*-

import requests
import MySQLdb
import datetime

today = datetime.date.today().strftime("%Y_%m_%d")

try:
    db = MySQLdb.connect("localhost", "root", "", "stockdb", charset="utf8")
except:
    print u"数据库stockdb无法连接!请检查后重试!"
    exit()
cursor = db.cursor()



#cursor.execute("DROP TABLE %s IF EXISTS %s;" % (today, today))

#cursor.execute("DROP TABLE %s;" % today)



sql = "CREATE TABLE %s (sn CHAR(20) ,股票名字  CHAR(50),今日开盘价  FLOAT,昨日收盘价 FLOAT,当前价格 FLOAT,今日最高价 FLOAT,今日最低价 FLOAT,竞买价 FLOAT ,竞卖价 FLOAT ,成交的股票数 FLOAT ,成交金额 FLOAT ,买一手数 FLOAT, 买一报价 FLOAT,买二手数 FLOAT, 买二报价 FLOAT,买三手数 FLOAT, 买三报价 FLOAT,买四手数 FLOAT, 买四报价 FLOAT,买五手数 FLOAT, 买五报价 FLOAT,卖一手数 FLOAT, 卖一报价 FLOAT,卖二手数 FLOAT, 卖二报价 FLOAT,卖三手数 FLOAT, 卖三报价 FLOAT,卖四手数 FLOAT, 卖四报价 FLOAT,卖五手数 FLOAT, 卖五报价 FLOAT, 日期 CHAR(50), 时间 CHAR(50));" % today

#sql = "CREATE TABLE %s (gp  CHAR(20),jz  FLOAT);" % today

try:
    cursor.execute(sql)
except:
    cursor.execute("DROP TABLE %s;" % today)
    cursor.execute(sql)
#idn = 0

def check_stock(sn):
    #global idn
    stock_response = requests.get('http://hq.sinajs.cn/list=%s' % sn)
    if stock_response:
        stock_text = stock_response.text
        stock_code_list = stock_text.split("\"")
        if len(stock_code_list) == 3:
            stock_code = stock_code_list[1]
            stock_fina_list = stock_code.split(",")
            if len(stock_fina_list) == 33:
                #print stock_fina_list
                stock_fina = []
                #stock_fina.append(stock_fina_list[0].encode('utf-8'))
                stock_fina.append(sn)
                for i in range(1, 30):
                    stock_fina.append(float(stock_fina_list[i]))
                stock_fina.append(stock_fina_list[30].encode('utf8'))
                stock_fina.append(stock_fina_list[31].encode('utf8'))
                stock_fina = tuple(stock_fina)
                print stock_fina
                #sq_n = "INSERT INTO %s (股票名字) VALUES ('%s');" % (today, stock_fina_list[0].encode('utf8'))
                sq = "INSERT INTO %s (sn, 今日开盘价, 昨日收盘价, 当前价格, 今日最高价, 今日最低价, 竞买价, 竞卖价, 成交的股票数, 成交金额, 买一手数, 买一报价, 买二手数, 买二报价, 买三手数, 买三报价, 买四手数, 买四报价, 买五手数, 买五报价, 卖一手数, 卖一报价, 卖二手数, 卖二报价, 卖三手数, 卖三报价, 卖四手数, 卖四报价, 卖五手数, 卖五报价, 日期, 时间) VALUES %s;" % (today, stock_fina)
                sq_m = "UPDATE %s SET 股票名字 = '%s' WHERE sn = '%s';" % (today, stock_fina_list[0].encode('utf8'), sn)
                #sq = "INSERT INTO %s(股票名字, 今日开盘价) VALUES ('%s', '%s');" % (today, stock_fina_list[0].encode('utf8'), float(stock_fina_list[1]))
                #cursor.execute("INSERT INTO %s ('股票名字', '今日开盘价') VALUES ('%s', '%s')" % (today, stock_fina_list[0], stock_fina_list[1]))
                print sq
                #cursor.execute(sq_n)
                cursor.execute(sq)
                cursor.execute(sq_m)

                db.commit()
                #idn += 1
# 上证
for shi in range(600000, 604000):
    shi = 'sh' + str(shi)
    check_stock(shi)

# 深证1
for szi in range(0, 2801):
    szi = 'sz' + str(szi).zfill(6)
    check_stock(szi)


for szj in range(300000, 3000517):
    szi = 'sz' + str(szi).zfill(6)
    check_stock(szi)