import pyspark
spark = pyspark.SparkContext()
spark_session = pyspark.sql.SparkSession(spark)
from pyspark.sql import functions as F
df = spark_session.read.csv("hdfs://localhost:9000/shape_stat.csv",inferSchema=True,header=True)

word_df = df[df['word']=="alarm clock"]
#word_df.show()
avg_recognised_count = word_df.groupBy(word_df.recognized).agg(F.avg(word_df.Total_Strokes)).collect()

print("##################.///////////")
print(round(avg_recognised_count[0]["avg(Total_Strokes)"],5))
print(round(avg_recognised_count[1]["avg(Total_Strokes)"],5))
#print("Average recognised is:",round(avg_recognised_count[0][1]))
#print("Average recognised is:",round(avg_recognised_count[1][1]))

#print("Avg Unrecognised count: ",avg_unrecognised_count)
#recognised_df = word_df[word_df['recognised']=]
#print("Word count is :",count_words)


