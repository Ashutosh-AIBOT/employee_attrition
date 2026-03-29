import sys
from pathlib import Path

_NOTEBOOKS_DIR = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
_PROJECT_ROOT = _NOTEBOOKS_DIR.parent if _NOTEBOOKS_DIR.name == "notebooks" else _NOTEBOOKS_DIR

if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from path_utils import (  # noqa: E402
    BASE,
    RAW,
    PROCESSED,
    MODELS,
    CHARTS,
    ensure_dirs,
    load_raw_csv,
    load_processed_csv,
)

ensure_dirs()
