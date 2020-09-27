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
      page_rank_contribution[node]+=contrib
  except Exception as e:
    # print("Task 2",line)
    continue
g = open("v1.txt","w")
for key in sorted(page_rank_contribution.keys()):
    g.write(str(functools.reduce(lambda x,y:x+y,page_rank_contribution[key])))
g.close()  