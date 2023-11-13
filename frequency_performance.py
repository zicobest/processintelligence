import pm4py
from pm4py.algo.conformance.alignments.process_tree.util import search_graph_pt_frequency_annotation
from pm4py.visualization.process_tree import visualizer as pt_visualizer

if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")
    proces_tree = pm4py.discover_process_tree_inductive(log)
    net, im, fm = pm4py.convert_to_petri_net(proces_tree)
    tree = pm4py.convert_to_process_tree(net, im, fm)
    print(tree)

    aligned_traces = pm4py.conformance_diagnostics_alignments(log, tree)
    tree = search_graph_pt_frequency_annotation.apply(tree, aligned_traces)
    gviz = pt_visualizer.apply(tree, parameters={"format": "png"}, variant=pt_visualizer.Variants.FREQUENCY_ANNOTATION)
    #pt_visualizer.view(gviz)
