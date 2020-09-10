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
  '''
  checks whether the record is clean or not

  word: Contains alphabets and whitespaces only
  countrycode: Contains only two uppercase letters
  recognized : Boolean value containing either "true" or "false"
  key_id: Numeric string containing 16 characters only
  drawing:Array containing n(>=1) strokes. Every stroke has exactly 2 arrays - where each array represents the ‘x’ and ‘y’ pixel coordinates respectively.
              
  input: dict
  returns: bool
  '''
  
  if not all(x.isalpha() or x.isspace() for x in record['word']):
    return False
  elif len(record['countrycode'])!=2 and record['countrycode'].isupper() or not record['countrycode'].isalpha():
    return False
  elif not (record['recognized']==True or record['recognized']==False or record['recognized']=="true" or record['recognized']=="false"):
    return False
  elif len(record['key_id'])!=16:
    return False
  elif not all(len(x)==2 for x in record['drawing']):
    return False
  else:
    return True


  # to do

for line in sys.stdin:
  # print(sys.argv[0],,sys.argv[2])
  record = json.loads(line)
  record_is_clean = is_clean(record)
  if record_is_clean:
    first_task(record,sys.argv[1])
  else:
    pass  


