import sys
import datetime
from datetime import timedelta
import matplotlib.pyplot as plt

algo = sys.argv[1]

def gettime(ti,tf):
    datetimeFormat = '%H:%M:%S.%f'
    diff = datetime.datetime.strptime(str(tf).strip(), datetimeFormat)\
    - datetime.datetime.strptime(str(ti).strip(), datetimeFormat)

    return float(diff.seconds)+float(diff.microseconds)/1000000

def getDateTimeObject(t):
    datetimeFormat = '%H:%M:%S.%f'
    temp = datetime.datetime.strptime(str(t).strip(), datetimeFormat)

    return temp


#To get the first timestamp which will be marked as 0 secs
with open("../Log/worker-log 1.txt", "r") as f:
    line =f.readline().strip('\n').split(" ")
    initialTime = getDateTimeObject(line[5])
    #print(initialTime)

with open("../Log/worker-log 2.txt", "r") as f:
    line =f.readline().strip('\n').split(" ")
    temp = getDateTimeObject(line[5])
    if(temp<initialTime):
        initialTime = temp

with open("../Log/worker-log 3.txt", "r") as f:
    line =f.readline().strip('\n').split(" ")
    temp = getDateTimeObject(line[5])
    if(temp<initialTime):
        initialTime = temp

    initialTime = str(initialTime)[11:]


time1 = []
worker1 = []
countWorker1 = 0
#worker1
with open("../Log/worker-log 1.txt", "r") as f:

    for lines in f.readlines():
        line = lines.strip('\n').split(" ")
        currentTime = line[5]

        #increment the current scheduled task for the worker
        if(line[0]=='Received'):
            countWorker1+=1
        elif(line[2]=='Completed'):
            countWorker1-=1

        time1.append(gettime(initialTime, currentTime))
        worker1.append(countWorker1)

time2 = []
worker2 = []
countWorker2 = 0
#worker2
with open("../Log/worker-log 2.txt", "r") as f:

    for lines in f.readlines():
        line = lines.strip('\n').split(" ")
        currentTime = line[5]

        #increment the current scheduled task for the worker
        if(line[0]=='Received'):
            countWorker2+=1
        elif(line[2]=='Completed'):
            countWorker2-=1

        time2.append(gettime(initialTime, currentTime))
        worker2.append(countWorker2)


time3 = []
worker3 = []
countWorker3 = 0
#worker3
with open("../Log/worker-log 3.txt", "r") as f:

    for lines in f.readlines():
        line = lines.strip('\n').split(" ")
        currentTime = line[5]

        #increment the current scheduled task for the worker
        if(line[0]=='Received'):
            countWorker3+=1
        elif(line[2]=='Completed'):
            countWorker3-=1

        time3.append(gettime(initialTime, currentTime))
        worker3.append(countWorker3)

if(algo=='LL'):
    algostr='Least Loaded'
elif(algo=='RR'):
    algostr='Round Robin'
else:
    algostr='Random'


#calculate the mean job and task time
djob = dict()
dtask = dict()


with open("../Log/Master-log "+algo+".txt","r") as fm:
    for lines in fm.readlines():

        #sender part
        l = lines.split(" ")
        #print(l)
        if(l[0]=='Received' and l[1]=='Job'):
            djob[l[2]] = l[4]
        elif(l[0]=='sending' and l[1]=='task'):
            dtask[l[2]] = l[6]
        elif(l[0]=='Completed'):
            djob[l[2]] = float(gettime(djob[l[2]],l[4]))
        elif(l[0]=='Received' and l[1]=='task'):
            dtask[l[2]] = float(gettime(dtask[l[2]],l[4]))
        else:
            pass


LLjob = []
LLtasks = []

for i in djob:
    LLjob.append(djob[i])
for i in dtask:
    LLtasks.append(dtask[i])

LLtasks = sorted(LLtasks)
LLjob = sorted(LLjob)


if(len(LLtasks)%2==0):
    print("Median time taken by tasks in "+algostr+" is :    ",LLtasks[int(len(LLtasks)/2)])
else:
    print("Median time taken by tasks in "+algostr+" is :    ",LLtasks[int((len(LLtasks)+1)/2)])

if(len(LLjob)%2==0):
    print("Median time taken by jobs in "+algostr+" is :    ",LLjob[int(len(LLjob)/2)])
else:
    print("Median time taken by jobs in "+algostr+" is :    ",LLjob[int((len(LLjob)+1)/2)])

print("Average time taken by jobs in "+algostr+" is :  ",sum(LLjob)/len(LLjob))

print("Average time taken by tasks in "+algostr+" is :  ",sum(LLtasks)/len(LLtasks))


plot1 = plt.figure('Scheduling algorithm : '+algostr)
plt.plot(time1, worker1, label="Worker 1")
plt.plot(time2, worker2, label="Worker 2")
plt.plot(time3, worker3, label="Worker 3")
plt.xlabel('Time(sec)')
plt.ylabel('Number of tasks running')
plt.title('Time vs Number of tasks scheduled per worker')
plt.legend()
plt.show()
