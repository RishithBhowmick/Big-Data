import sys

nodes = dict()
for line in sys.stdin:
  try:
    from_node,to_node = line.split("\t",1)
    to_node = to_node.strip("\n")
    to_node = to_node.strip("\r")
    if from_node not in nodes.keys():
      nodes[from_node] = list()
      nodes[from_node].append(to_node)
    else:
      nodes[from_node].append(to_node)
  except Exception as e:
    # print("Task 2",line)
    continue
f=open("v.txt","w")
for key in sorted(nodes.keys()):
  print(key,sep=" ",end=" ")
  print(*nodes[key],sep=",")
  f.write("1\n")
f.close()  
