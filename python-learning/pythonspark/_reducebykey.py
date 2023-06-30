from pyspark import *
import os

os.environ['PYSPARK_PYTHON'] = "D:/Program Files/python/python3.11.3/python.exe"
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf= conf)

rdd= sc.parallelize([('a',10),('a',10),('b',10),('b',10),('b',10),('b',10),('c',10)])
result = rdd.reduceByKey(lambda a,b: a+b)
print(result.collect())
