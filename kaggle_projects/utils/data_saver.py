import os
import json
import pickle
import pandas as pd

class DataSaver:
    def __init__(self, project_name, base_path="projects"):
        self.project_folder = project_name.lower().replace(" ", "_")
        self.base_path = os.path.join(base_path, self.project_folder, "data")

    def _resolve_path(self, data_type: str, filename: str) -> str:
        data_type = data_type.lower()
        valid_types = ["input", "processed", "artifacts", "output"]
        if data_type not in valid_types:
            raise ValueError(f"Invalid data type. Choose from {valid_types}")
        os.makedirs(os.path.join(self.base_path, data_type), exist_ok=True)
        return os.path.join(self.base_path, data_type, filename)

    def save(self, obj, data_type: str, filename: str):
        """
        Save object to appropriate folder.
        Supports: .csv (pandas), .json, .pkl
        """
        path = self._resolve_path(data_type, filename)

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
