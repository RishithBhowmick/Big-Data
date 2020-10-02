#!/usr/bin/python3
import sys


for line in sys.stdin:
  try:
      if line.startswith("#"):
          continue
      else:
          ele = line.split("\t")
          from_node = ele[0]

          if(len(ele)!= 1):
            to_node = ele[1].strip("\r\n")
            print(f"{from_node}\t{to_node}")            
  except Exception as e:
      continue
