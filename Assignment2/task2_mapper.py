import sys

#insert full path to v here
f = open("v.txt","r")


for line in sys.stdin:
    try:
        pagerank = f.readline()
        to_nodes = line.split(" ")[1]
        num_nodes = len(to_nodes)
        node_contribution = float(pagerank)/num_nodes
        for node in to_nodes.split(","):
            print(f"{node}\t{node_contribution}")
    except Exception as e:
        print("Task2 mapper error: ",e)