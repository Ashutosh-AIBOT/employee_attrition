import os
from pathlib import Path
from typing import Tuple

import pandas as pd


def resolve_base() -> str:
    cwd = Path.cwd()
    if (cwd / "data").exists() and (cwd / "models").exists():
        return str(cwd)
    if cwd.name == "notebooks" and (cwd.parent / "data").exists():
        return str(cwd.parent)
    if "__file__" in globals():
        here = Path(__file__).resolve().parent
        return str(here)
    return str(cwd)


def get_paths() -> Tuple[str, str, str, str, str]:
    base = resolve_base()
    raw = os.path.join(base, "data", "raw")
    processed = os.path.join(base, "data", "processed")
    models = os.path.join(base, "models")
    charts = os.path.join(base, "charts")
    return base, raw, processed, models, charts


def ensure_dirs() -> None:
    _, _, processed, models, charts = get_paths()
    os.makedirs(processed, exist_ok=True)
    os.makedirs(models, exist_ok=True)
    os.makedirs(charts, exist_ok=True)


def load_raw_csv(filename: str, **kwargs) -> pd.DataFrame:
    _, raw, _, _, _ = get_paths()
    path = os.path.join(raw, filename)
    return pd.read_csv(path, **kwargs)


def load_processed_csv(filename: str, **kwargs) -> pd.DataFrame:
    _, _, processed, _, _ = get_paths()
    path = os.path.join(processed, filename)
    return pd.read_csv(path, **kwargs)


BASE, RAW, PROCESSED, MODELS, CHARTS = get_paths()
