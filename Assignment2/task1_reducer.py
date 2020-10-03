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
    
    #to capture nodes that have only incoming nodes
    #I think this is the problem which doesnt need to be handled as that node wont be there in the dataset
    # as in, eg 0 haso only incoming links, it will appear only on the RHS of the dataset
    if to_node not in keys:
      nodes[to_node] = list()

  except Exception as e:
    continue

f=open(sys.argv[1],"w")
for key in sorted(nodes.keys()):
  l=sorted(nodes[key])
  if len(l)!=0:
    print(key,sep=" ",end=" ")
    print(*l,sep=",")
  f.write(f"{key},1\n") 
# writing ALL the existing nodes and initialising their page rank to 1