import pandas as pd
import os
import glob

dir_path = "Footprint Data/Ticket Daily Report/2023"
files = os.listdir(dir_path)
all_csv_files = glob.glob(os.path.join(dir_path, "*.csv"))
all_csv_files.sort(key=os.path.getmtime)

df = pd.read_csv(all_csv_files[-1], encoding="ISO-8859-1")

def returnColumn(column):
    dfStatus = df[column]
    return dfStatus.to_json()


