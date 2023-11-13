import pm4py
if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")
    process_tree = pm4py.discover_process_tree_inductive(log)

    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    pm4py.view_bpmn(bpmn_model)