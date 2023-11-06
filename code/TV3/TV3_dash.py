import pandas as pd
import os
import glob
# KPI page backend

# iterate through folders in Footprints Data and store in a dataframe
"""
Date Created    Account     Product     Status

"""
def returnFootprintsData(inputValue):
    footprints_path = "code/Footprints Data/Ticket Daily Report"
    all_folders = os.listdir(footprints_path)
    li = []
    dates_column = []
    for folder in all_folders:
        folder_path = os.listdir(f"{footprints_path}/{folder}")
        for file in folder_path:
            if(file.endswith('.csv') != True):
                data_xls = pd.read_excel(f"{footprints_path}/{folder}/{file}", index_col=None)
                data_xls.to_csv(f"{footprints_path}/{folder}/{file}.csv", index=False)
                os.remove(f"{footprints_path}/{folder}/{file}")
            else:
                report_date = file[:10]
                dates_column.append(report_date)
                dates_df = pd.DataFrame(dates_column)
                df = pd.read_csv(f"{footprints_path}/{folder}/{file}", encoding="ISO-8859-1")
                df["Date Created"] = None
                for i in range(len(dates_column)):
                    if (report_date == dates_column[i]):
                        df["Date Created"] = report_date
                     
                li.append(df)
    footprints_dataframe = pd.concat(li, ignore_index=True)
    returnedData = footprints_dataframe[inputValue]
    return returnedData.to_json()
