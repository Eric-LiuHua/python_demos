# -*- coding: UTF-8 -*- 
#! /usr/bin/python3
__author__ = 'Liu.Eric'
 
import sys
import csv
import os


import ssq
import dlt
import linear

# 获取数据在保存到目录
def save_data(rows,file):
   
  #with open(file, "w" if not os.path.exists(data_ssq_file) else "a", newline='') as f:
 
  with open(file, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
     
    f.close()
    print ("write over")


if __name__ == '__main__':
  print("python3 main !")
  # 双色球 数据集名称
  data_ssq_file = '/Users/Liuhua/Projects/pythonprojects/caipiao/data/ssq.csv'
  data_dlt_file = '/Users/Liuhua/Projects/pythonprojects/caipiao/data/dlt.csv'
  ssq_rows = ssq.get_500_data()
  save_data(ssq_rows , data_ssq_file)
  
 
  #dlt_rows = dlt.get_500_data(100)
  #save_data(dlt_rows , data_dlt_file)
  #print(dlt_rows)

  #linear.get_data(data_ssq_file)
  
  print("end of work!")

