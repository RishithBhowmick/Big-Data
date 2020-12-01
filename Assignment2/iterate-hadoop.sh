#!/bin/sh
CONVERGE=1
rm v* log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
$HADOOP_HOME/bin/hdfs dfs -rm -r /output* 

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-streaming-3.2.1.jar \
-mapper "/home/rishith/Desktop/Big-Data/Assignment2/task1_mapper.py " \
-reducer "/home/rishith/Desktop/Big-Data/Assignment2/task1_reducer.py '/home/rishith/Desktop/Big-Data/Assignment2/v'"  \
-input /dataset-A2 \
-output /output1 #has adjacency list


while [ "$CONVERGE" -ne 0 ]
do
	$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-streaming-3.2.1.jar \
	-mapper "/home/rishith/Desktop/Big-Data/Assignment2/task2_mapper.py '/home/rishith/Desktop/Big-Data/Assignment2/v' " \
	-reducer /home/rishith/Desktop/Big-Data/Assignment2/task2_reducer.py \
	-input /output1 \
	-output /output2
	touch v1
	hadoop fs -cat /output2/* > /home/rishith/Desktop/Big-Data/Assignment2/v1
	CONVERGE=$(python3 check_conv.py >&1)
	$HADOOP/bin/hdfs dfs -rm -r /output2
	echo $CONVERGE

done
