import pm4py
from pm4py.algo.filtering.dfg import dfg_filtering

# Directly-follows graphs can contain a huge number of activities and paths, with some of them being outliers

# how to filter on the activities and paths of the graph, keeping a subset of its behavior.
# The most frequent activities according to the percentage are kept, along with
# all the activities that keep the graph connected. If a percentage of 0 % is specified

# then the most frequent activity (and the activities keeping the graph connected) is retrieved.
# Specifying 0.2 as in the example, we want to keep the 20% of activities
#  The filter is applied concurrently to the DFG, to the start activities, to the end activities,
#  and to the dictionary containing the activity occurrences. In such way, consistency is kept
if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")
    dfg, sa, ea = pm4py.discover_directly_follows_graph(log)
    activities_count = pm4py.get_event_attribute_values(log, "concept:name")

    dfg, sa, ea, activities_count = dfg_filtering.filter_dfg_on_activities_percentage(dfg, sa, ea, activities_count,
                                                                                      0.2)

    #dfg, sa, ea, activities_count = dfg_filtering.filter_dfg_on_paths_percentage(dfg, sa, ea, activities_count, 0.2)
    print(dfg, sa, ea, activities_count)
