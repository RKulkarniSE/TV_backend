import pandas as pd
import os
import glob

# iterate through folders in Footprints Data and store in a dataframe
def returnFootprintsData():
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
                df = pd.read_csv(f"{footprints_path}/{folder}/{file}", encoding="ISO-8859-1")
                df["Date Created"] = None
                for i in range(len(dates_column)):
                    if (report_date == dates_column[i]):
                        df["Date Created"] = report_date
                     
                li.append(df)
    footprints_dataframe = pd.concat(li, ignore_index=True)
    return footprints_dataframe

# return ticket range
def returnTopSites(start_date, end_date):
    data = returnFootprintsData()
    data["Date Created"] = pd.to_datetime(data["Date Created"])
    result_df = data[(data['Date Created'] >= start_date) & (data['Date Created'] <= end_date)]

    # return the most frequent element, by 'Account'
    word_series = pd.Series(result_df['Account'])
    word_count = word_series.value_counts()[:5].index.tolist()
    print(word_count)

returnTopSites('2023-01-20', '2023-01-27')