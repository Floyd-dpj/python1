from pyspark import SparkConf, SparkContext
import os


os.environ['PYSPARK_PYTHON'] = "D:/Program Files/python/python3.11.3/python.exe"
os.environ['HADOOP_HOME'] = "D:/Program Files/hadoop-3.0.0"
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf=conf)


rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd.saveAsTextFile("D:/output8")