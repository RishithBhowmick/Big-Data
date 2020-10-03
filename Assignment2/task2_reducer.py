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
    print(e)

for key in sorted(page_rank_contribution.keys()):
    pagerank = functools.reduce(lambda x,y:x+y,page_rank_contribution[key]) 
    pagerank = 0.15000+(0.85000*pagerank)
    # print(f"{key},{round(pagerank,5)}") 
    print("%s,%.5f"%(key,pagerank)) 
