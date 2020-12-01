#!/usr/bin/python3
import sys
import json
import datetime
import re
 

def euclidean_dist(x,y):
    return (x**2+y**2)**0.5

def second_task(record,target_word,dist):
    l=euclidean_dist(record["drawing"][0][0][0],record["drawing"][0][1][0])
    if record["word"]==target_word and l>dist:
        print("%s\t%s"%(record['countrycode'],1))
    else:
      pass
    
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
    lis=[len(j[0])==len(j[1]) for j in record['drawing']]
    if list(set(lis))!=[True]:
      return False
    return True   
  except Exception as e:
    return False


  # to do

for line in sys.stdin:
  try:
    record = json.loads(line)
    record_is_clean = is_clean(record)
    if record_is_clean:
      second_task(record,sys.argv[1],int(sys.argv[2]))
    else:
      continue
  except Exception as e:
    continue


