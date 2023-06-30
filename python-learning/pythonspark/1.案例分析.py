from pyspark import *
import os

os.environ['PYSPARK_PYTHON'] = "D:/Program Files/python/python3.11.3/python.exe"
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf= conf)

rdd = sc.textFile("D:/hello.txt")
rdd2 = rdd.flatMap(lambda x: x.split(" "))

rdd3 = rdd2.map(lambda data:(data,1))
rdd4 = rdd3.reduceByKey(lambda a,b: a+b)
print(rdd4.collect())