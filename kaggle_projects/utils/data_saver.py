import os
import json
import pickle
import pandas as pd

class DataSaver:
    def __init__(self, project_name, base_path="Projects"):
        self.project_folder = project_name.lower().replace(" ", "_")
        self.base_path = os.path.join(base_path, self.project_folder, "data")

    def _resolve_path(self, data_type: str, filename: str) -> str:
        data_type = data_type.lower()
        valid_types = ["input", "processed", "artifacts", "output"]
        if data_type not in valid_types:
            raise ValueError(f"Invalid data type. Choose from {valid_types}")
        return os.path.join(self.base_path, data_type, filename)

    def save(self, obj, data_type: str, filename: str):
        """
        Save object to appropriate folder.
        Supports: .csv (pandas), .json (dict), .pkl (any)
        """
        path = self._resolve_path(data_type, filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)

        if filename.endswith(".csv") and isinstance(obj, pd.DataFrame):
            obj.to_csv(path, index=False)
        elif filename.endswith(".json") and isinstance(obj, dict):
            with open(path, "w") as f:
                json.dump(obj, f, indent=4)
        elif filename.endswith(".pkl"):
            with open(path, "wb") as f:
                pickle.dump(obj, f)
        else:
            raise ValueError("Unsupported file format or object type.")

        print(f"✅ Saved: {path}")

    def load(self, data_type: str, filename: str):
        """
        Load object from appropriate folder.
        Supports: .csv, .json, .pkl
        """
        path = self._resolve_path(data_type, filename)

        if not os.path.exists(path):
            raise FileNotFoundError(f"{path} not found.")

        if filename.endswith(".csv"):
            return pd.read_csv(path)
        elif filename.endswith(".json"):
            with open(path, "r") as f:
                return json.load(f)
        elif filename.endswith(".pkl"):
            with open(path, "rb") as f:
                return pickle.load(f)
        else:
            raise ValueError("Unsupported file format for loading.")

