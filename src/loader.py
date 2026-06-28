import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"


def load_json(file_name: str):
    path = DATA_DIR / file_name
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)