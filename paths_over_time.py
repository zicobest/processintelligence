import pm4py
import os

if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")

    from pm4py.algo.transformation.log_to_interval_tree import algorithm as log_to_interval_tree

    # The dotted chart is a classic visualization of the events inside an event log across different dimensions.
    # Each event of the event log is corresponding to a point. The dimensions are projected on a graph having
    # X axis: the values of the first dimension are represented there.
    # Y-axis: the values of the second dimension are represented there.
    pm4py.view_dotted_chart(log, format="svg")
