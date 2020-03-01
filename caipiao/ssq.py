# -*- coding: UTF-8 -*- 
#! /usr/bin/python3
__author__ = 'Liu.Eric'
import requests 
from lxml import etree
import matplotlib.pyplot as pyplot
from pandas import Series
from random  import choice
import time;  # 引入time模块




# 获取双色球的数据，默认范围，start=00001 ，end= 153（2019年07月04日）前置当年年份就是最新数据了
def get_500_data(start = '00001', end = '200'):
  year = time.strftime("%y", time.localtime())
  end=year + '' + end
  rows = []
  # 期号，红1，红2，红3，红4，红5，红6，蓝球，奖池，一等奖数量，一等奖金额，二等奖数量，二等奖金额，总投注，开奖日期
  headers =['QH','R1','R2','R3','R4','R5','R6','B','JC','L1C','L1A','L2C','L2A','ZTE','Kdate']

  rows.append(headers)

  url = "http://datachart.500.com/ssq/history/newinc/history.php?start=%s&end=%s"%(start,end)
  print(url)

  response = requests.get(url)
  response = response.text
  selector = etree.HTML(response)
  t = selector.xpath('//tbody[@id="tdata"]/tr[@class="t_tr1"]')
  
  for i in t:
    row = []
    # 期号
    row.append(i.xpath('td/text()')[0]) 
    # 红球1-6
    row = row + i.xpath('td/text()')[1:7]
    # 篮球
    row.append(i.xpath('td/text()')[7])
  
    # 奖池，一等奖数量，一等奖金额，二等奖数量，二等奖金额，总投注，开奖日期
    row = row + i.xpath('td/text()')[9:15]
    rows.append(row)

  
  print(rows)
  print(len(rows))
  
  return rows 
    



# 机选功能 
def get_random():
    #初始化号码池
    red_init_numbers = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
               "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33"]
    blue_init_balls  = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16"]
 
    #初始化机选集合
    red_numbers = []
    blue_numbers = [] 

    #机选篮球一个
    blue_numbers.append(choice(blue_init_balls))
    # 33选6
    while len(red_numbers) < 6:
        temp_number = choice(red_init_numbers)
        if temp_number in red_numbers :
            continue
        else :
            red_numbers.append(temp_number)
    
    red_numbers.sort()
    return ','.join(red_numbers) + '|' + blue_numbers[0]



if __name__ == '__main__':
  print("cmd： python3 ./pc/s's'q.py  ")
  print(get_random())

  print('end ssq work.!')
  
 
      