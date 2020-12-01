#!/usr/bin/python3
import sys


all_keys = dict()
for line in sys.stdin:
    line = line.strip()
    
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        if word not in all_keys.keys():
            all_keys[word]=1
        else:
            all_keys[word]+=1
    except Exception as e:
        continue        

try:
    for i in sorted(all_keys.items(),key=lambda x:x[0]):
        print(i[1])
except Exception as e:  
    pass