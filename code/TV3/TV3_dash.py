import pandas as pd
import os
import glob
# KPI page backend

# iterate through folders in Footprints Data and store in a dataframe
"""
Date (YY/MM)    Account     Product     Status

"""
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
            df = pd.concat([df, dates_df], axis=1)
            df.dropna(inplace=True)
            df.rename(columns={0:"Date Created"}, inplace=True)
            li.append(df)

frame = pd.concat(li)
print(frame.iloc[:100, :10])

