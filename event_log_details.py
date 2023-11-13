import pandas as pd
import datetime as dt


def import_csv(file_path):
    event_log = pd.read_csv(file_path, sep=";")
    num_events = len(event_log)
    num_case = len(event_log.CASE_ID.unique())
    print("Number of events:{}\n Number of cases:{}".format(num_events, num_case))


if __name__ == "__main__":
    import_csv("Pizza_Event.csv")
