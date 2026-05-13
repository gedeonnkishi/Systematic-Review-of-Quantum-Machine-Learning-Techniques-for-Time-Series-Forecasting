"""Reproducibility helpers."""

from __future__ import annotations

import json
import os
import platform
import random
from pathlib import Path
from typing import Any

import numpy as np


def set_seed(seed: int) -> None:
    """Set common random seeds.

    Torch seed setting is attempted only if torch is installed.
    """
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    try:
        import torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except Exception:
        pass


def export_metadata(path: str | Path, extra: dict[str, Any] | None = None) -> None:
    """Export environment metadata for reviewer inspection."""
    metadata = {
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "processor": platform.processor(),
    }
    try:
        import numpy, pandas, scipy, sklearn, matplotlib
        metadata.update({
            "numpy": numpy.__version__,
            "pandas": pandas.__version__,
            "scipy": scipy.__version__,
            "sklearn": sklearn.__version__,
            "matplotlib": matplotlib.__version__,
        })
    except Exception:
        pass
    try:
        import torch
        metadata.update({
            "torch": torch.__version__,
            "cuda_available": torch.cuda.is_available(),
            "cuda_device_count": torch.cuda.device_count() if torch.cuda.is_available() else 0,
        })
    except Exception:
        pass
    if extra:
        metadata.update(extra)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
