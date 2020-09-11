#!/usr/bin/python3
# import numpy as np
import sys
import json
import datetime
import re


def first_task(record,word):

  is_recognised = record['recognized']
  if is_recognised is True and record["word"]==word:
    print("%s\t%d"%("Recognized",1))   

  elif is_recognised is False:
    time=datetime.date(int(record['timestamp'].split(' ')[0].split('-')[0]),int(record['timestamp'].split(' ')[0].split('-')[1]),int(record['timestamp'].split(' ')[0].split('-')[2])).weekday()
    if time in range(5,7) and record["word"]==word:
        print("%s\t%d"%("UnRecognized",1))   
    
def is_clean(record):
  try:
    if not all(x.isalpha() or x.isspace() for x in record['word']):
      return False
    elif len(record['countrycode'])!=2 or not record['countrycode'].isupper() or not record['countrycode'].isalpha():
        return False
    elif not (record['recognized']==True or record['recognized']==False or record['recognized']=="true" or record['recognized']=="false"):
        return False
    elif len(record['key_id'])!=16 or not record['key_id'].isdigit():
        return False
    elif not all(len(x)==2 for x in record['drawing']) or record['drawing']==[]:
        return False
    elif not all(len(x)==2 for x in record['drawing']) or record['drawing']==[]:
      return False
    else:
      return True
  except Exception as e:
    return False    


  # to do

for line in sys.stdin:
  try:
    record = json.loads(line)
    record_is_clean = is_clean(record)
    if record_is_clean:
      first_task(record,sys.argv[1])
    else:
      continue
  except Exception as e:
    continue    


