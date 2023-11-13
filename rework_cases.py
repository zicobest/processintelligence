import pm4py
from pm4py.statistics.rework.cases.log import get as cases_rework_get
#rework at the case level the number of events of a case having an activity which has appeared previously in the case
if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")
    log = pm4py.convert_to_event_log(log)

    dictio = cases_rework_get.apply(log)

    print(dictio)