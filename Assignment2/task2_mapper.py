import sys

#insert full path to v here
page_rank_dict = dict()
f = open(sys.argv[1],"r")
for i in f.readlines():
    ele = i.split(",")
    node = ele[0]
    if len(ele)!=1:
        page_rank = float(ele[1].strip("\n"))
        page_rank_dict[node] = page_rank


for line in sys.stdin:
    try:
        ele = line.split(" ")
        node1 = ele[0]
        to_nodes = ele[1].strip("\n")
        to_nodes = to_nodes.split(",")
        num_nodes = len(to_nodes)    

        node_contribution = page_rank_dict[node1]/num_nodes

        for node in to_nodes:
            # print("Node is:",node,".")
            print(f"{node}\t{node_contribution}")
    except Exception as e:
        continue
