from pyspark import *
import os

os.environ['PYSPARK_PYTHON'] = "D:/Program Files/python/python3.11.3/python.exe"
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf= conf)

rdd = sc.textFile("D:/2011年1月销售数据.txt")
rdd2 = rdd.flatMap(lambda x: x.split(" "))
print(rdd2.collect())