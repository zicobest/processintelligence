import matplotlib
import pandas as pd
import pm4py

df = pm4py.read_xes("to_xes_file.xes")

dfg = pm4py.discover_dfg(df)
# represents all possible activities, and represents all multisets over sequences of activities)
print(dfg[0])
print(dfg[1])  # start activities
print(dfg[2])  # end activities

# %matplotlib inline i need python 3.11 before i can use this
import networkx as nx
import itertools as it

G = nx.DiGraph()
alphabet = set(list(it.chain.from_iterable([[a, b] for (a, b) in dfg[0]]))).union(dfg[1].keys()).union(dfg[2].keys())
G.add_nodes_from(alphabet)  # adding nodes
nx.draw(G,  with_labels=True)
