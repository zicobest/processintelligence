import pm4py
import pandas as pd
import datetime as dt


def import_xes(file_path):
    event_log = pm4py.read_xes(file_path)
    start = pm4py.get_start_activities(event_log)
    end = pm4py.get_end_activities(event_log)

    print("Start activites:{}\n End activities:{}".format(start, end))

    print(event_log['case:concept:name'].nunique())

if __name__== "__main__":
    import_xes("to_xes_file.xes")


