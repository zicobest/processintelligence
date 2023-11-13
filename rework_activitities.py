import pm4py
from pm4py.statistics.rework.cases.log import get as cases_rework_get

# rework at the case level the number of events of a case having an activity which has appeared previously in the case
#The rework statistic permits to identify the activities which have been repeated during the same process execution. This shows the underlying inefficiencies in the process
if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")

    rework = pm4py.get_rework_cases_per_activity(log)

    print(rework)
