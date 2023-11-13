import pm4py
if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")
    dfg, start_activites,end_activites =pm4py.discover_dfg(log)
    pm4py.view_dfg(dfg, start_activites,end_activites)