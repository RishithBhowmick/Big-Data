import sys

#insert full path to v here
f = open("v.txt","r")

i=0
for line in sys.stdin:
    try:
        if not line:
            continue
        node,pagerank = f.readline().split(",")
        to_nodes = line.split(" ")[1]
        to_nodes = to_nodes.strip("\r\n")
        try:
            num_nodes = len(to_nodes.split(","))
        except Exception as e:
            num_nodes = 1    
        node_contribution = float(pagerank)/num_nodes
        for node in to_nodes.split(","):
                print("%s\t%f"%(node,node_contribution))
    except Exception as e:
        print("Task2 mapper error: ",e,"node and line is",line)