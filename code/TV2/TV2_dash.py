import pandas as pd

df = pd.read_csv('./report_test.csv', encoding="ISO-8859-1")

def returnColumn(column):
    dfStatus = df[column]
    return dfStatus.to_json()


