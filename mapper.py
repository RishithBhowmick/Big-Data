import sys
import json


for line in sys.stdin:

  word = "airplane"
  # print(line,type(line))
  record=  json.loads(line) #not sure
  # print(record['recognized'])
  if record['word']=='airplane':
  
  # i.update({'word':'airplane'})
    word1=record['word']
    # time=datetime.date(int(record['timestamp'].split(' ')[0].split('-')[0]),int(record['timestamp'].split(' ')[0].split('-')[1]),int(record['timestamp'].split(' ')[0].split('-')[2])).weekday()
    if word=="airplane": 
      if record['recognized'] is True:
        print('%s\t%s'%("recognized",1))
      elif record['recognized'] is False:
        print('%s\t%s'%("not recognized and the day is a weekend day :P",1))

