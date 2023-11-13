import pm4py

if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")
    proces_tree = pm4py.discover_process_tree_inductive(log)
    #pm4py.view_process_tree(proces_tree)

    net1, im1, fm1 = pm4py.convert_to_petri_net(proces_tree)
    pm4py.view_petri_net(net1, im1, fm1)

    # The alpha+ miner Extension of the alpha miner that handles length-one-loops and short loops.

    # the main events and loops connection for better visibility

    net3, im3, fm3 = pm4py.discover_petri_net_alpha(log)
    pm4py.view_petri_net(net3, im3, fm3)
