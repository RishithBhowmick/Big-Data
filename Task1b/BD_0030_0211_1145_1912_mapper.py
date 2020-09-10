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
  elif len(record['countrycode'])!=2 or not record['countrycode'].isupper() or not record['countrycode'].isalpha():
      return False
  elif not (record['recognized']==True or record['recognized']==False or record['recognized']=="true" or record['recognized']=="false"):
      return False
  elif len(record['key_id'])!=16 or not record['key_id'].isdigit():
      return False
  elif not all(len(x)==2 for x in record['drawing']) or record['drawing']==[]:
      return False
  elif all(len(x)==2 for x in record['drawing']):
    for j in record['drawing']:
      lis=[len(x) for x in j]
      if len(list(set(lis)))!=1:
          return False
      else:
        for k in j:
          if not all(isinstance(item, int) for item in k):
              return False
    return True


  # to do

for line in sys.stdin:
  # print(sys.argv[0],,sys.argv[2])
  record = json.loads(line)
  record_is_clean = is_clean(record)
  if record_is_clean:
    second_task(record,sys.argv[1],int(sys.argv[2]))
  else:
    pass  


