from pyspark import *
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/python/python3.11.3/python.exe"
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf= conf)

rdd = sc.textFile("D:/2011年1月销售数据.txt")
rdd3 = rdd.flatMap(lambda x: x.split(" "))
# list = []
# for a in rdd3.collect():
#     a=list(a)
#     print(a)
#     list.append(a)
rdd5 = rdd3.sortBy(lambda data: data[2], ascending=False, numPartitions=1)

print(rdd5.collect())