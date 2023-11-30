from zipfile import ZipFile
import os
import glob
import requests
from bs4 import BeautifulSoup
import wget
import sched
import time

def LoadingData():
    url = "http://nemweb.com.au/Reports/Current/Dispatch_SCADA"  
    temp_url = "http://nemweb.com.au"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.find_all('a')

    # Filter links that end with '.zip'
        zip_links = [link.get('href') for link in links if link.get('href') and link.get('href').endswith('.zip')]

        if zip_links:
        # Get the last zip link
            last_zip_link = zip_links[-1]
        # Construct the absolute URL if the link is relative
            if not last_zip_link.startswith('http'):
                last_zip_link = temp_url + last_zip_link
 
            zip_file_save_directory = "./Zipped/"
            print(f"Downloading {last_zip_link}...")
            downloaded_file = wget.download(last_zip_link, out=zip_file_save_directory)
        
            print("Download completed.")
        else:
            print("No zip files found on the page.")
    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)

# unzips

    unzipped_dir = "./Unzipped/"
    with ZipFile(downloaded_file, 'r') as zObject:
        file_pattern = "*.zip"
        file_paths = glob.glob(os.path.join(zip_file_save_directory, file_pattern))
        zObject.extractall(path=unzipped_dir)

    for zip in file_paths:
        os.remove(zip)

    dir_path = "./Unzipped"
    files = os.listdir("./Unzipped")
    all_csv_files = glob.glob(os.path.join(dir_path, "*.CSV"))
    all_csv_files.sort(key=os.path.getmtime)
    if all_csv_files and len(files) > 2:
        oldest_csv = all_csv_files[0]
        os.remove(oldest_csv)
        print(f"Deleted oldest file: {oldest_csv}")
    else:
        print("Directory has at least one file. Cannot delete")

LoadingData()
scheduler = sched.scheduler(time.time, time.sleep)
interval = 300

def run_periodically(scheduler):
    LoadingData()
    scheduler.enter(interval, 1, run_periodically, (scheduler,))

scheduler.enter(0, 1, run_periodically, (scheduler,))
scheduler.run()