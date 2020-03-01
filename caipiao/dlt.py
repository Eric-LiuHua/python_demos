# -*- coding: UTF-8 -*- 
#! /usr/bin/python3
__author__ = 'Liu.Eric'

import time
import requests 
from lxml import etree
import matplotlib.pyplot as pyplot
from pandas import Series
from random import choice 


# 获取大乐透的数据，默认范围， total=10000  大乐透是limit 到发方式
def get_500_data(total = 10000):
 
  rows = []
  # 期号，红1，红2，红3，红4，红5，篮1，蓝2，奖池，一等奖数量，一等奖金额，二等奖数量，二等奖金额，总投注，开奖日期
  headers =['QH','R1','R2','R3','R4','R5','B1','B2','JC','L1C','L1A','L2C','L2A','ZTE','Kdate']

  rows.append(headers)

  url = "http://datachart.500.com/dlt/history/newinc/history.php?limit=%s&sort=0"%(total)
  print(url)

  response = requests.get(url)
  response = response.text
  selector = etree.HTML(response)
  t = selector.xpath('//tbody[@id="tdata"]/tr[@class="t_tr1"]')
  
  for i in t:
    row = []
    # 期号
    row.append(i.xpath('td/text()')[0]) 
    # 红球 1-5
    row = row + i.xpath('td/text()')[1:6]
    # 篮球 1-2
    row = row + i.xpath('td/text()')[6:8]
  
    # 奖池，一等奖数量，一等奖金额，二等奖数量，二等奖金额，总投注，开奖日期
    row = row + i.xpath('td/text()')[8:15]
    rows.append(row)

  return rows


 # 机选功能 

#机选
def get_random():
    #初始化号码池
    red_init_numbers = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
               "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35"]
    blue_init_balls  = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
 
    #初始化机选集合
    red_numbers = []
    blue_numbers = [] 

    
    
    # 35选5
    while len(red_numbers) < 5:
        temp_number = choice(red_init_numbers)
        if temp_number in red_numbers :
            continue
        else :
            red_numbers.append(temp_number)


    #机选篮球 12 选2 
    while len(blue_numbers) < 2:
        temp_number = choice(blue_init_balls)
        if temp_number in blue_numbers :
            continue
        else :
            blue_numbers.append(temp_number)
    
    #排序
    red_numbers.sort()
    blue_numbers.sort()

    return ','.join(red_numbers) + '|' + ','.join(blue_numbers)


if __name__ == '__main__':
  print("cmd： python3 ./pc/dlt.py  ")
  print(get_random())

  print('end dlt work.!')
  
