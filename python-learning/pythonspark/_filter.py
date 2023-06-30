from pyspark import *
import os

os.environ['PYSPARK_PYTHON'] = "D:/Program Files/python/python3.11.3/python.exe"
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf= conf)

rdd = sc.textFile("D:/hello.txt")
rdd3 = rdd.flatMap(lambda x: x.split(" "))
rdd4 = rdd3.filter(lambda data: data == "itheima")
print(rdd4.collect())


rdd1= sc.parallelize([1,2,3,4,5])
rdd2 = rdd1.filter(lambda num: num % 2 == 0)
print(rdd2.collect())
