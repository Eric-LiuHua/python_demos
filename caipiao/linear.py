#!/usr/bin/python
# -*- coding:UTF-8 -*-
 
#导入需要的包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator
from sklearn import datasets,linear_model
from sklearn.linear_model import LogisticRegression


df=[]

#读取文件
def get_data(csv_name):
  df = pd.read_table(csv_name,header=None,sep=',')
  
  tdate = sorted(df.loc[:,0])

  print(df)

  





