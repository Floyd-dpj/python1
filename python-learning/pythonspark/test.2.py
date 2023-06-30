from pyspark import *
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf= conf)

# rdd1= sc.parallelize([1,2,3,4,5])
# rdd2= sc.parallelize((1,2,3,4,5,6))
# rdd3= sc.parallelize('ffff')
# rdd4= sc.parallelize({1,2,3,4,5,6})
# rdd5= sc.parallelize({'key':'value1', 'key2':'value2'})
# rdd.collect() 查看rdd的数据内容
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())

rdd = sc.textFile("D:/orders.txt")
print(rdd.collect())

sc.stop()