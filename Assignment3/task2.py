import findspark
import pyspark
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").getOrCreate()
shape = spark.read.option("header",True).csv('/content/drive/My Drive/shape.csv')
shape_stat = spark.read.option("header",True).csv('/content/drive/My Drive/shape_stat.csv')
from pyspark.sql.functions import *
shape = shape.alias('shape')
shape_stat = shape_stat.alias('shape_stat')
s=shape.join(shape_stat, shape.key_id == shape_stat.key_id).select(shape["*"],shape_stat["timestamp"],shape_stat['recognized'],shape_stat['Total_Strokes'])
word = 'angel'
k = 8
valoutput = s.filter((s.recognized=='False') & (s.Total_Strokes>k) & (s.word == word)).groupBy('countrycode').count().show()