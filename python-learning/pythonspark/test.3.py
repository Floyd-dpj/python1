from pyspark import *
import os

os.environ['PYSPARK_PYTHON'] = "D:/Program Files/python/python3.11.3/python.exe"
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf= conf)


rdd1= sc.parallelize([1,2,3,4,5])
def func(data):
    return data*10+5

rdd2= rdd1.map(func)

print(rdd2.collect())
sc.stop()