import pandas as pd

# Read the three CSV files
df1 = pd.read_csv('Pizza_Event.csv', sep=";")
df2 = pd.read_csv('Pizza_Customer Info.csv', sep=";")
df3 = pd.read_csv('Pizza_Case.csv', sep=";")

# Join the DataFrames based on a common column, for example, 'Customer_ID'
joined_df = df1.set_index('CASE_ID').join(df2.set_index('Customer_ID')).join(df3.set_index('Customer_ID'))

# Reset the index to create a new index column
joined_df.reset_index(inplace=True)

# Save the joined DataFrame to a new CSV file
joined_df.to_csv('joined_files.csv', index=False)

df = pd.read_csv("joined_files.csv")
#df.fillna('Unknown', inplace=True)
# Drop unnecessary columns
columns_to_drop = ["Unnamed: 3", "Unnamed: 4"]
df.drop(columns_to_drop, axis=1, inplace=True)
#df = df.dropna(axis=1)
# Print the resulting DataFrame
df.fillna('Unknown', inplace=True)
print(df)
df.to_csv("new_join_all_sort.csv")
"""
# Read the CSV files
df1 = pd.read_csv('Pizza_Event.csv', sep=";")
df2 = pd.read_csv('Pizza_Customer Info.csv', sep=";")

# Join dataframes based on CustomerID column
joined_df = df1.set_index('CASE_ID').join(df2.set_index('Customer_ID'))

# Save joined dataframe to a new CSV file
joined_df.to_csv('joined.csv')

# Read the joined CSV file
df = pd.read_csv("joined.csv")
df.fillna('Unknown', inplace=True)
# Drop unnecessary columns
columns_to_drop = ["Unnamed: 0", "Unnamed: 3", "Unnamed: 4", "Customer_Type"]
df.drop(columns_to_drop, axis=1, inplace=True)

# Print the resulting DataFrame
print(df)
print(df.columns)
# dc.drop(["Unnamed: 0"], axis=1)
# all empty columns with Unknown i mean the columns which are empty with unknown
# df.fillna('Unknown', inplace=True)

df.to_csv("new_join.csv")
# print(df)
"""
