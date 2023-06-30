from pyspark import *
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/python/python3.11.3/python.exe"
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf= conf)

rdd = sc.textFile("D:/hello.txt")
rdd3 = rdd.flatMap(lambda x: x.split(" "))
rdd4 = rdd3.distinct()
print(rdd4.collect())