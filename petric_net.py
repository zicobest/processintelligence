import pm4py
import pandas as pd
# Observe that the Petri net consists of two different type of nodes, i.e., cirlces and rectangles. We refer to the circles as places and we refer

# to the rectangles as transitions. Furthermore, notice that, a place can only be connected (by means of an arc) to a transition. Similarly,

# a transition can only be connected (by means of an arc) to a place. Hence, places never connect directly to places and transitions never connect directly to transitions.
log = pm4py.format_dataframe(pd.read_csv("Pizza_Event.csv", sep=";"), case_id="CASE_ID", activity_key="ACTIVITY_EN",
                             timestamp_key="EVENTTIME")
pn, im, fm = pm4py.discover_petri_net_inductive(log)
pm4py.view_petri_net(pn, im, fm)
pm4py.check_soundness(pn, im, fm)