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
for folder in all_folders:
    folder_path = os.listdir(f"{footprints_path}/{folder}")
    for file in folder_path:
        if(file.endswith('.csv') != True):
            data_xls = pd.read_excel(f"{footprints_path}/{folder}/{file}", index_col=None)
            data_xls.to_csv(f"{footprints_path}/{folder}/{file}.csv", index=False)
            os.remove(f"{footprints_path}/{folder}/{file}")
            
        else:
            df = pd.read_csv(f"{footprints_path}/{folder}/{file}", encoding="ISO-8859-1")
            li.append(df)

frame = pd.concat(li)
print(frame.head())

