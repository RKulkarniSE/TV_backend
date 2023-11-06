import pandas as pd
import os
import glob

folder_path = "code/Footprints Data/Ticket Daily Report"
folders = os.listdir(folder_path)
latest_folder = max(folders)

dir_path = f"{folder_path}/{latest_folder}"
files = os.listdir(dir_path)
all_csv_files = glob.glob(os.path.join(dir_path, "*.csv"))
all_csv_files.sort(key=os.path.getmtime)
latest_report = all_csv_files[-1]

df = pd.read_csv(latest_report, encoding="ISO-8859-1")

def returnColumn(column):
    dfStatus = df[column]
    return dfStatus.to_json()