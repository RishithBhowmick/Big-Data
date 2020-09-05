#!/usr/bin/python3
# import numpy as np
import sys
import json
import datetime


def first_task(record):

  is_recognised = record['recognized']
  if is_recognised is True and record["word"]=="airplane":
    print("%s\t%d"%("Recognized",1))   

  elif is_recognised is False:
    time=datetime.date(int(record['timestamp'].split(' ')[0].split('-')[0]),int(record['timestamp'].split(' ')[0].split('-')[1]),int(record['timestamp'].split(' ')[0].split('-')[2])).weekday()
    if time in range(5,7) and record["word"]=="airplane":
        print("%s\t%d"%("Not Recognized",1))   
    




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

  # to do

for line in sys.stdin:
  record = json.loads(line)
  second_task(record,"aircraft carrier",100)