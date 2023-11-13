import pandas as pd
import datetime as dt
import pm4py

df = pd.read_csv("new_join_all_sort.csv")
#df.drop(df.iloc[:, 0], axis=1, inplace=True)
print(df.columns)


# Assuming your DataFrame is named df
columns_to_drop = ['Unnamed: 0', 'index', 'Variant', 'Revenue', 'Customer_Type', '_CASE_KEY',  "Pizza Type", "Pizza Size"]

# Use the drop() function to remove the specified columns
df.drop(columns=columns_to_drop, inplace=True)
print(df.columns)
df.to_csv("database.csv")

