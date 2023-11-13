import pm4py
if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")
    dfg, sa, ea = pm4py.discover_directly_follows_graph(log)
    activities_count = pm4py.get_event_attribute_values(log, "concept:name")
    simulated_log= pm4py.play_out(dfg, sa, ea)
    alignment = pm4py.conformance_diagnostics_alignments(simulated_log, dfg, sa, ea)

    print(alignment)