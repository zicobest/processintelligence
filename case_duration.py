import os
import pm4py

if __name__ == "__main__":

    log = pm4py.read_xes("to_xes_file.xes")

    from pm4py.util import constants
    from pm4py.statistics.traces.generic.log import case_statistics

    x, y = case_statistics.get_kde_caseduration(log, parameters={
        constants.PARAMETER_CONSTANT_TIMESTAMP_KEY: "time:timestamp"})

    from pm4py.visualization.graphs import visualizer as graphs_visualizer

    gviz = graphs_visualizer.apply_plot(x, y, variant=graphs_visualizer.Variants.CASES)
    graphs_visualizer.view(gviz)

    gviz = graphs_visualizer.apply_semilogx(x, y, variant=graphs_visualizer.Variants.CASES)
    graphs_visualizer.view(gviz)
