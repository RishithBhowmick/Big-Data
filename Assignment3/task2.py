import findspark
import pyspark
import sys
findspark.init()
from pyspark.sql import SparkSession
if len(sys.argv)==5:

    spark = SparkSession.builder.master("local[*]").getOrCreate()
    shape = spark.read.option("header",True).csv(sys.argv[3])
    shape_stat = spark.read.option("header",True).csv(sys.argv[4])
    shape = shape.alias('shape')
    shape_stat = shape_stat.alias('shape_stat')
    s=shape.join(shape_stat, shape.key_id == shape_stat.key_id).select(shape["*"],shape_stat["timestamp"],shape_stat['recognized'],shape_stat['Total_Strokes'])
    k = 8
    valoutput = s.filter((s.recognized=='False') & (s.Total_Strokes<sys.argv[2]) & (s.word == sys.argv[1])).groupBy('countrycode').count().show()
    if not valoutput:
        print(0)
    else:
        for i in valoutput.rdd.collect():
            print(i['countrycode']+','+str(i['count']))
else:
    pass        

