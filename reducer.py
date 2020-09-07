#!/usr/bin/python3
from operator import itemgetter
import sys

previous_word = word = None
current_count = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # print(word,count)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if previous_word == word:
        current_count += count
    else:
        if previous_word:
            # write result to STDOUT
            print(current_count)
        current_count = count
        previous_word = word   

# do not forget to output the last word if needed!
if previous_word == word:
    print (current_count)