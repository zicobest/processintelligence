import pandas as pd
import pm4py
import datetime as dt

log = pm4py.format_dataframe(pd.read_csv("Pizza_Event.csv", sep=";"), case_id="CASE_ID", activity_key="ACTIVITY_EN",
                             timestamp_key="EVENTTIME")
print("the beginning of some processes")
filter0 = len(pm4py.filter_start_activities(log, {"Start baking pizza"}))
print("Start baking pizza:", filter0)

filter1 = len(pm4py.filter_start_activities(log, {"Order by phone"}))
print("Order by phone:", filter1)
filter2 = len(pm4py.filter_start_activities(log, {"Order at the counter (shop)"}))
print("Order at the counter (shop):", filter2)
filter3 = len(pm4py.filter_start_activities(log, {"Start preparing pizza"}))
print("Start preparing pizza:", filter3)
filter4 = len(pm4py.filter_start_activities(log, {"Approve order website"}))
print("Approve order website:", filter4)
filter5 = len(pm4py.filter_start_activities(log, {"Receive order website"}))
print("Receive order website:", filter5)
filter6 = len(pm4py.filter_start_activities(log, {"Call Customer"}))
print("Call Customer:", filter6)

# filter end  event number for a particular order
print("these are the end if events and the number of times they occurred")
filter7 = len(pm4py.filter_end_activities(log, {"Payment customer"}))
print("Payment customer:", filter7)
filter8 = len(pm4py.filter_end_activities(log, {"Baking pizza ready"}))
print("Baking pizza ready:", filter8)
filter9 = len(pm4py.filter_end_activities(log, {"Pizza received"}))
print("Pizza received:", filter9)
filter10 = len(pm4py.filter_end_activities(log, {"Start baking pizza"}))
print("Start baking pizza:", filter10)
filter11 = len(pm4py.filter_end_activities(log, {"Pizza arrives at customer"}))
print("Pizza arrives at customer:", filter11)
filter12 = len(pm4py.filter_end_activities(log, {"Start preparing pizza"}))
print("Start preparing pizza:", filter12)
filter13 = len(pm4py.filter_end_activities(log, {"Departure pizza"}))
print("Departure pizza:", filter13)
