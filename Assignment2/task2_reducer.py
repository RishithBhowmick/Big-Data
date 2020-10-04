#!/usr/bin/python3
import sys

page_rank_contribution = dict()
for line in sys.stdin:
  try:
    node,contrib = line.split("\t",1)
    contrib = float(contrib)
    if node not in page_rank_contribution.keys():
      page_rank_contribution[node] = contrib
    else:
      page_rank_contribution[node]+=contrib
  except Exception as e:
    pass

for key in sorted(page_rank_contribution.keys()):
    pagerank = page_rank_contribution[key]
    pagerank = 0.15+(0.85*pagerank)
    print("%s,%.5f"%(key,pagerank)) 
