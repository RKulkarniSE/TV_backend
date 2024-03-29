import pandas as pd
import os

# list of products to be searched in the Footprints Data
# you can add products to this list if you want
products_list = {'OPC', 'RuggedCom', 'Security Server', 'T3000', 'NAS', 'S7', 'CS3000', 'AS3000', 'McAfee', 'Thin Client'}

# iterate through folders in Footprints Data and store in a dataframe
def footprintsData():
    footprints_path = "Footprints Data/Ticket Daily Report"    
    all_folders = [f for f in os.listdir(footprints_path) if os.path.isdir(os.path.join(footprints_path, f))]
    
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
    return word_count.to_json()

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
    result_set = []
    for word in word_series:
        for product in product_set:
            if (product in word):
                result_set.append(product)

    result_set = pd.Series(result_set).value_counts()
    return result_set.to_json()
