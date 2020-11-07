import pyspark
import sys
spark = pyspark.SparkContext()
spark_session = pyspark.sql.SparkSession(spark)
from pyspark.sql import functions as F
# print("Arguments length .......: ",len(sys.argv))
if len(sys.argv)==4:

	df = spark_session.read.csv(sys.argv[3],inferSchema=True,header=True)

	word_df = df[df['word']==sys.argv[1]]
	avg_recognised_count = word_df.groupBy(word_df.recognized).agg(F.avg(word_df.Total_Strokes)).collect()

	
	if not avg_recognised_count:
		print("{:.5f}".format(0))
		print("{:.5f}".format(0))
	#print(avg_recognised_count)
	else:
		print(round(avg_recognised_count[0]["avg(Total_Strokes)"],5))
		print(round(avg_recognised_count[1]["avg(Total_Strokes)"],5))
else:
	pass

#print("Average recognised is:",round(avg_recognised_count[0][1]))
#print("Average recognised is:",round(avg_recognised_count[1][1]))

#print("Avg Unrecognised count: ",avg_unrecognised_count)
#recognised_df = word_df[word_df['recognised']=]
#print("Word count is :",count_words)


# print()