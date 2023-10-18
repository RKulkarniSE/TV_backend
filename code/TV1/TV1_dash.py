import pandas as pd
import os

renamedDUIDs = {'Bayswater 1', 'Bayswater 2', 'Bayswater 3','Bayswater 4', 'Barron Gorge 1','Barron Gorge 2', 'Stanwell 1','Stanwell 2','Stanwell 3', 'Stanwell 4','Callide B1','Callide B2','Tarong 1', 'Tarong 2','Tarong 3','Tarong 4', 'Kogan Creek',
                         'Braemar 2', 'Oakey 1','Oakey 2', 'Vales Point 5', 'Vales Point 6','Mt Piper 1', 'Mt Piper 2','Uranquinty 1', 'Uranquinty 2', 'Uranquinty 3', 'Uranquinty 4','Tallawarra', 'Loy Yang A2', 'Hallett',
                         'Osborne', 'Mortlake 1', 'Mortlake 2', 'Laverton North 1', 'Laverton North 2'}
def StationCapacity():
    
    # load facilities.csv data
    dfFac = pd.read_csv('./facilities.csv')
    dfFacName = dfFac[['Facility Name', 'Generator Capacity (MW)']]
    filtered_df = dfFacName[dfFacName['Facility Name'].isin(renamedDUIDs)]
    return filtered_df.to_json()
        

def DataframeConversion(paramStr):
    files = os.listdir("./Unzipped/")
    dfFac = pd.read_csv('./facilities.csv')

    for file in files:
        file_path = os.path.join("./Unzipped/", file)
    if file.endswith('.CSV'):
       df = pd.read_csv(file_path, skiprows=1)
       
    renaming_DUIDs_dictionary = { 'BW01':'Bayswater 1', 'BW02':'Bayswater 2', 'BW03':'Bayswater 3', 'BW04':'Bayswater 4', 'BARRON-1':'Barron Gorge 1', 'BARRON-2':'Barron Gorge 2', 'STAN-1':'Stanwell 1', 'STAN-2':'Stanwell 2', 'STAN-3':'Stanwell 3', 'STAN-4':'Stanwell 4', 
                                  'CALL_B_1':'Callide B1', 'CALL_B_2':'Callide B2', 'TARONG#1':'Tarong 1', 'TARONG#2':'Tarong 2', 'TARONG#3':'Tarong 3', 'TARONG#4':'Tarong 4', 'KPP_1':'Kogan Creek',
                         'BRAEMAR2':'Braemar 2', 'OAKEY1':'Oakey 1', 'OAKEY2':'Oakey 2', 'VP5':'Vales Point 5', 'VP6':'Vales Point 6', 'MP1':'Mt Piper 1', 'MP2':'Mt Piper 2', 'URANQ11':'Uranquinty 1', 'URANQ12':'Uranquinty 2', 'URANQ13':'Uranquinty 3', 'URANQ14':'Uranquinty 4', 'TALWA1':'Tallawarra', 'LYA2':'Loy Yang A2',
                           'AGLHAL':'Hallett','OSB-AG':'Osborne', 'MORTLK11':'Mortlake 1', 'MORTLK12':'Mortlake 2', 'LNGS1':'Laverton North 1', 'LNGS2':'Laverton North 2'}

    
    df['DUID'] = df['DUID'].replace(renaming_DUIDs_dictionary)
    
    selectedDUID_rows = df[df['DUID'].isin(renamedDUIDs)]
    selectedDUID_rows = selectedDUID_rows.reset_index()
    selectedDUID_rows = pd.concat([selectedDUID_rows, dfFac], axis=1)
    selectedDUID_rows = selectedDUID_rows.drop(['index', 'Facility Name'], axis=1)
    selectedRows = selectedDUID_rows[paramStr]
    df.dropna(inplace=True)

    return selectedRows.to_json()

def run_periodically(sc, interval):
    DataframeConversion('SCADAVALUE')
    sc.enter(interval, 1, run_periodically, (sc,))
    return DataframeConversion('SCADAVALUE')