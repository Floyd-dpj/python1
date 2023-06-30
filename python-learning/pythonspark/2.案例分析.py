from pyspark import *
import os
import json

os.environ['PYSPARK_PYTHON'] = "D:/Program Files/python/python3.11.3/python.exe"
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf= conf)

rdd = sc.textFile("D:/orders.txt")
rdd1 = rdd.flatMap(lambda x: x.split("|"))
rdd2 = rdd1.map(lambda x : json.loads(x))
rdd3 = rdd2.map(lambda x:(x['areaName'], int(x['money'])))
rdd4 = rdd3.reduceByKey(lambda a,b: a+b)
rdd5 = rdd4.sortBy(lambda x:x[1],ascending=False,numPartitions=1)
print("需求1的结果：",rdd5.collect())

rdd6 = rdd2.map(lambda x : x["category"]).distinct()
print("需求2的结果：", rdd6.collect())

rdd7 = rdd2.filter(lambda x: x["areaName"] == "北京")
rdd8 = rdd7.map(lambda x: x["category"]).distinct()
print("需求3的结果",rdd8.collect())


