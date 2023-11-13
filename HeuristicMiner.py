import pm4py

if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")
    map = pm4py.discover_heuristics_net(log)
    pm4py.view_heuristics_net(map)
