import pm4py

log = pm4py.read_xes("to_xes_file.xes")
filter = pm4py.filter_variants(log, [
    ["Order by phone", "Start preparing pizza", " Start baking pizza", "Baking pizza ready", "Plan route",
     "Departure pizza",
     "Pizza arrives az customer", "Payment customer"]])
# print(filter)

filter2 = pm4py.filter_directly_follows_relation(log, [("Order by phone", "Payment customer")])
print(filter2)
