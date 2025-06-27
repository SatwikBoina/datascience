import os
import sys
import shutil
import yaml
import subprocess
from zipfile import ZipFile

def slug_to_folder(slug: str) -> str:
    return slug.replace("/", "-")

def load_kaggle_config():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "kaggle_downloader", "config.yaml")
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)
    return cfg.get("datasets", {})

def download_dataset(slug, data_dir="data"):
    folder_name = slug_to_folder(slug)
    dataset_path = os.path.join(data_dir, folder_name)
    zip_path = os.path.join(data_dir, f"{folder_name}.zip")

    if not os.path.exists(dataset_path):
        print(f"Downloading dataset {slug}...")
        subprocess.run(["kaggle", "datasets", "download", "-d", slug, "-p", data_dir], check=True)

        # Rename downloaded zip if needed
        downloaded_zip = os.path.join(data_dir, slug.split("/")[1] + ".zip")
        if os.path.exists(downloaded_zip):
            os.rename(downloaded_zip, zip_path)

        # Extract
        with ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(dataset_path)
        print(f"Extracted to {dataset_path}")
    else:
        print(f"Dataset {slug} already downloaded.")
    return dataset_path

def copy_csv_to_project_input(dataset_path, project_input_path):
    csv_files = [f for f in os.listdir(dataset_path) if f.endswith(".csv")]
    if not csv_files:
        print(f"No CSV files found in {dataset_path}")
        return

    os.makedirs(project_input_path, exist_ok=True)

    for csv_file in csv_files:
        src = os.path.join(dataset_path, csv_file)
        dst = os.path.join(project_input_path, csv_file)
        shutil.copy2(src, dst)
        print(f"Copied {csv_file} to {project_input_path}")

def create_project_env_yaml(base_path, project_name, extra_packages=None):
    if extra_packages is None:
        extra_packages = ["scikit-learn", "matplotlib", "seaborn", "jupyterlab"]

    lines = []
    lines.append(f"name: {project_name}")
    lines.append("channels:")
    lines.append("  - conda-forge")
    lines.append("dependencies:")

    for pkg in extra_packages:
        lines.append(f"  - {pkg}")

    lines.append("  - pip")
    lines.append("  - pip:")
    lines.append("    - kaggle")

    env_yaml_content = "\n".join(lines)
    env_yaml_path = os.path.join(base_path, "env.yaml")
    with open(env_yaml_path, "w") as f:
        f.write(env_yaml_content)
    print(f"Created minimal env.yaml at {env_yaml_path}")

def create_project_structure(project_name):
    folder_name = project_name.lower().replace(" ", "_")
    base_path = os.path.join("projects", folder_name)

    folders = {
        "data": ["input", "processed", "artifacts", "output"],
        "config": [],
        "src": [],
        "notebooks": [],
        "utils": []
    }

    for folder, subfolders in folders.items():
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        for sub in subfolders:
            os.makedirs(os.path.join(path, sub), exist_ok=True)

    # config/config.yaml
    config_path = os.path.join(base_path, "config", "config.yaml")
    with open(config_path, "w") as f:
        f.write("# Configuration for the project\n")

    # src/main.py
    main_py_path = os.path.join(base_path, "src", "main.py")
    with open(main_py_path, "w") as f:
        f.write(
            "# Entry point for the project\n"
            "def main():\n"
            "    print('Hello from main.py')\n\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        )

    # notebooks/starter_notebook.ipynb
    notebook_path = os.path.join(base_path, "notebooks", "starter_notebook.ipynb")
    with open(notebook_path, "w") as f:
        f.write("""{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
""")

    # README.md
    readme_path = os.path.join(base_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# {project_name}\n\nProject description goes here.\n")

    print(f"Project structure created at: {base_path}")

    # Create minimal project env.yaml with extras
    extra_deps = ["scikit-learn", "matplotlib", "seaborn", "jupyterlab"]
    create_project_env_yaml(base_path, folder_name, extra_deps)

    # Download datasets from kaggle_downloader/config.yaml and copy CSVs
    datasets = load_kaggle_config()
    if project_name in datasets:
        slug = datasets[project_name]
        dataset_path = download_dataset(slug)
        project_input_path = os.path.join(base_path, "data", "input")
        copy_csv_to_project_input(dataset_path, project_input_path)
    else:
        print(f"⚠️ No dataset found for project '{project_name}' in kaggle_downloader/config.yaml")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python setup_project.py \"project name\"")
        sys.exit(1)

    project_name = sys.argv[1]
    create_project_structure(project_name)
