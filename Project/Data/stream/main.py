from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import json
# from pprint import pprint

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = SparkContext("local[2]", "NetworkWordCount")
sc.setLogLevel("OFF")
ssc = StreamingContext(sc, 1)


lines = ssc.socketTextStream("localhost", 6100)

# words = lines.flatMap(lambda line: json.loads(line))

lines.pprint()
ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate