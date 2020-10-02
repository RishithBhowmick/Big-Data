#!/usr/bin/python3
import sys
import functools

page_rank_contribution = dict()
for line in sys.stdin:
  try:
    node,contrib = line.split("\t",1)
    contrib = float(contrib)
    if node not in page_rank_contribution.keys():
      page_rank_contribution[node] = list()
      page_rank_contribution[node].append(contrib)
    else:
      page_rank_contribution[node].append(contrib)
  except Exception as e:
    continue

for key in sorted(page_rank_contribution.keys()):
    pagerank = functools.reduce(lambda x,y:x+y,page_rank_contribution[key]) 
    pagerank = 0.15+(0.85*pagerank)
    print(f"{key},{round(pagerank,5)}") 
