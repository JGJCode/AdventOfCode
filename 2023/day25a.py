import networkx as nx
from collections import defaultdict
from matplotlib import pyplot as plt
wireMap=defaultdict(list)
with open('day25.txt') as file:
    for line in file:
        s,d=line.rstrip().split(':')
        wireMap[s]=d.split()
graph=nx.from_dict_of_lists(wireMap)
for u,v in nx.minimum_edge_cut(graph):
    graph.remove_edge(u,v)
u,v=nx.connected_components(graph)
print(len(u)*len(v))
