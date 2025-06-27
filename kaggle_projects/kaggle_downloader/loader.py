import os
import pandas as pd
from kaggle_downloader.downloader import download_all_datasets

def load_all_csvs() -> dict:
    dataset_paths = download_all_datasets()
    dataframes = {}

    for name, path in dataset_paths.items():
        csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]

        if not csv_files:
            print(f"No CSV found in {path}, skipping.")
            continue

        df = pd.read_csv(os.path.join(path, csv_files[0]))
        dataframes[name] = df

    return dataframes
