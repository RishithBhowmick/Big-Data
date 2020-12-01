from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
import json
# from pprint import pprint

# Create a local StreamingContext with two working thread and batch interval of 1 second
def checkMatch(event):
	if 'wyId' in event.keys():
		return True
	return False

def checkEvent(event):
	if 'eventId' in event.keys():
		return True
	return False

sc = SparkContext("local[2]", "FPL Analytics")
sc.setLogLevel("OFF")
ssc = StreamingContext(sc, 1)

#to read data as dataframe
sc_sql = SparkSession(sc)

teams_info = sc.textFile("file:///home/rishith/Desktop/Big-Data/Project/Data/teams.csv")

# teams_df = teams_info.toDF()
# teams_info.collect()

lines = ssc.socketTextStream("localhost", 6100)

all_events = lines.map(lambda line: json.loads(line))

match_info = all_events.filter(checkMatch)

events_info = all_events.filter(checkEvent)

match_info.pprint()

ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate