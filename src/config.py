"""Configuration helpers for the benchmark package."""

from pathlib import Path
import yaml


def load_config(path: str | Path = "configs/benchmark_config.yaml") -> dict:
    """Load the YAML benchmark configuration.

    Parameters
    ----------
    path:
        Path to the benchmark YAML file.

    Returns
    -------
    dict
        Parsed configuration dictionary.
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
