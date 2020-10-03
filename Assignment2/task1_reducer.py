#!/usr/bin/python3
import sys

nodes = dict()
# need to use a data structure to collect all the existing nodes
for line in sys.stdin:
  try:
    from_node,to_node = line.split("\t",1)
    to_node = to_node.strip("\n")

     # collect the existing keys
    keys = nodes.keys()
    if from_node not in keys:
      nodes[from_node] = list()
      nodes[from_node].append(to_node)
    else:
      nodes[from_node].append(to_node)
    
    
  except Exception as e:
    continue

f=open(sys.argv[1],"w")
for key in sorted(nodes.keys()):
  print(key,sep=" ",end=" ")
  print(*sorted(nodes[key]),sep=",")
  f.write(f"{key},1\n") 
# writing ALL the existing nodes and initialising their page rank to 1