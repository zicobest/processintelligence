import pm4py
import pandas as pd

if __name__ == "__main__":
    # log = pm4py.format_dataframe(pd.read_csv("Pizza_Event.csv", sep=";"), case_id="CASE_ID", activity_key="ACTIVITY_EN",
    # timestamp_key="EVENTTIME")
    log = pm4py.read_xes("to_xes_file.xes")
    filter_log = pm4py.filter_between(log, "Order by phone", "Start preparing pizza")

    print(filter_log)
