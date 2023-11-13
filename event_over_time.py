import pm4py
from pm4py.algo.filtering.log.attributes import attributes_filter

if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")
    x, y = attributes_filter.get_kde_date_attribute(log, attribute="time:timestamp")

    from pm4py.visualization.graphs import visualizer as graphs_visualizer

    gviz = graphs_visualizer.apply_plot(x, y, variant=graphs_visualizer.Variants.DATES)
    graphs_visualizer.view(gviz)
