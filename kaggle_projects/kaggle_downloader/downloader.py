import os
import subprocess
import yaml
from zipfile import ZipFile

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")
DATA_DIR = "data"

def load_config():
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)["datasets"]

def slug_to_folder(slug: str) -> str:
    return slug.replace("/", "-")

def download_all_datasets():
    datasets = load_config()
    paths = {}

    os.makedirs(DATA_DIR, exist_ok=True)

    for name, slug in datasets.items():
        folder_name = slug_to_folder(slug)
        dataset_path = os.path.join(DATA_DIR, folder_name)
        zip_file = os.path.join(DATA_DIR, f"{folder_name}.zip")

        if not os.path.exists(dataset_path):
            print(f"Downloading {slug}...")
            subprocess.run(["kaggle", "datasets", "download", "-d", slug, "-p", DATA_DIR], check=True)

            downloaded_zip = os.path.join(DATA_DIR, slug.split("/")[1] + ".zip")
            if os.path.exists(downloaded_zip):
                os.rename(downloaded_zip, zip_file)

            with ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(dataset_path)

            print(f"Extracted to: {dataset_path}")
        else:
            print(f"Dataset {name} already exists at {dataset_path}")

        paths[name] = dataset_path

    return paths
