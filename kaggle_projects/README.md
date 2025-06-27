# Kaggle Projects

This folder contains my Kaggle-related data science projects, experiments, and datasets.  
The structure and utilities are designed to streamline downloading datasets using the Kaggle API, managing data, and loading data efficiently.

---

## Folder Structure


---

## Setup Instructions

### 1. Kaggle API Credentials

- Download your `kaggle.json` API token from [Kaggle Account](https://www.kaggle.com/settings).
- Place it in your home directory under `.kaggle/`:
  
```bash
  mkdir -p ~/.kaggle
  mv /path/to/kaggle.json ~/.kaggle/
  chmod 600 ~/.kaggle/kaggle.json
```
### 2. Create a Conda environment
```bash
    conda env create -f env.yaml
    conda activate kaggle_env
```
### 3. Add Project name and it's data slug
    1. go to the kaggle_downloader\config.yaml
    2. Mention the project_folder : slug in the yaml file

### 4. Set up a Project Directory
Call the project folder name here.
```bash
    python setup_project.py "Titanic Survival Prediction"
```

