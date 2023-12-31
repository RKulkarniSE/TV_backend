import pandas as pd
import os
import glob

folder_path = "Footprints Data/Ticket Daily Report"
folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
latest_folder = max(folders)

dir_path = f"{folder_path}/{latest_folder}"
all_csv_files = glob.glob(os.path.join(dir_path, "*.csv"))
all_csv_files.sort(key=os.path.getmtime)
latest_report = all_csv_files[-1]

df = pd.read_csv(latest_report, encoding="ISO-8859-1")
df = df.reindex(index=df.index[::-1])
df = df.reset_index(drop=True)

def returnColumn(column):
    dfStatus = df[column]
    return dfStatus.to_json()

def footprints_run_periodically(sc, interval, column):
    dfStatus = df[column]
    sc.enter(interval, 1, footprints_run_periodically, (sc,))
    return dfStatus.to_json()