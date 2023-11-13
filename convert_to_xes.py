import pandas as pd
import pm4py

if __name__ == "__main__":
    event_log = pm4py.format_dataframe(pd.read_csv("Pizza_Event.csv", sep=";"), case_id="CASE_ID", activity_key= "ACTIVITY_EN",
                                       timestamp_key="EVENTTIME")
    pm4py.write_xes(event_log, "to_xes_file.xes")
