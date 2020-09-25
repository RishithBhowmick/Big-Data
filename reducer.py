#!/usr/bin/python3
from operator import itemgetter
import sys

previous_word = word = None
current_count = 0

# input comes from STDIN
all_keys = dict()
for line in sys.stdin:
    line = line.strip()
    
    word, count = line.split('\t', 1)
    
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        if previous_word == word:
            current_count += count
        else:
            if previous_word:
                # write result to STDOUT
                print(current_count)
            current_count = count
            previous_word = word
    except Exception as e:
        continue           

# do not forget to output the last word if needed!
try:
    if previous_word == word:
        print("%s\t%s")
except Exception as e:
    pass