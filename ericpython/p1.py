# coding= utf-8

from __future__ import print_function

from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession


def getdata1(spark):
    df = spark.read.load('/Users/Liuhua/Projects/scalaproject/sparkexamples/src/main/resources/users.parquet')
    df.select('name','favorite_color').show()
    df.show()


if __name__ == '__main__':


    spark = SparkSession.builder.config(conf = SparkConf().setAppName('eric').setMaster('local')).getOrCreate()

    print(121)
    getdata1(spark)

    spark.stop()

