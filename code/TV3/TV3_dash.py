import pandas as pd
import os
import glob
import time

products_list = {'OPC', 'RuggedCom', 'Security Server', 'T3000', 'NAS', 'S7', 'CS3000', 'AS3000', 'McAfee', 'Thin Client'}

# iterate through folders in Footprints Data and store in a dataframe
def footprintsData():
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

def topSites(start_date, end_date):
    data = footprintsData()
    data["Date Created"] = pd.to_datetime(data["Date Created"])
    result_df = data[(data['Date Created'] >= start_date) & (data['Date Created'] <= end_date)]

    number_of_results = 5
    word_series = pd.Series(result_df['Account'])
    word_count = word_series.value_counts()[:number_of_results].index.tolist()
    return word_count

def ticketPerSite(start_date, end_date):
    data = footprintsData()
    data["Date Created"] = pd.to_datetime(data["Date Created"])
    result_df = data[(data['Date Created'] >= start_date) & (data['Date Created'] <= end_date)]

    word_series = pd.Series(result_df['Account'])
    word_count = word_series.value_counts()
    return word_count

def ticketByPriority(start_date, end_date):
    data = footprintsData()
    data["Date Created"] = pd.to_datetime(data["Date Created"])
    result_df = data[(data['Date Created'] >= start_date) & (data['Date Created'] <= end_date)]
    """
    PRIORITIES:
    1-ASAP      2-HIGH      3-MED       4-LOW
    """
    word_series = pd.Series(result_df['Priority'])
    word_count = word_series.value_counts()
    return word_count.to_json()

def ticketByProduct(start_date, end_date):
    data = footprintsData()
    data["Date Created"] = pd.to_datetime(data["Date Created"])
    result_df = data[(data['Date Created'] >= start_date) & (data['Date Created'] <= end_date)]

    word_series = pd.Series(result_df['Title'])
    product_set = set(products_list)
    for word in word_series:
        for product in product_set:
            if (product in word):
                print(word)

ticketByProduct('2021-02-11', '2021-02-11')