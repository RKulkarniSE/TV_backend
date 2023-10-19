import pandas as pd

"""
Convert the reports csv file into a pandas dataframe

Extract and sort relevant data
Status, Ticket ID, Account, Product , Date Submitted, Assignees
"""
df = pd.read_csv('./report_test.csv', encoding="ISO-8859-1")

def returnColumn(column):
    dfStatus = df[column]
    return dfStatus.to_json()

print(returnColumn("Date Submitted"))

