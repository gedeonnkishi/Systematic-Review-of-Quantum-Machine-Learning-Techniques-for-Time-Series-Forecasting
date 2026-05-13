"""Data pipeline utilities.

The functions below enforce the anti-leakage protocol used in the manuscript:
chronological split, train-only scaling, and sliding-window construction.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple
import numpy as np
from sklearn.preprocessing import StandardScaler


@dataclass(frozen=True)
class ChronologicalSplit:
    train: np.ndarray
    validation: np.ndarray
    test: np.ndarray


def chronological_split(series: np.ndarray, train_ratio: float = 0.70, val_ratio: float = 0.15) -> ChronologicalSplit:
    """Split a univariate or multivariate series chronologically.

    No random shuffling is applied.
    """
    if series.ndim == 1:
        series = series.reshape(-1, 1)
    n = len(series)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)
    train = series[:n_train]
    validation = series[n_train:n_train + n_val]
    test = series[n_train + n_val:]
    return ChronologicalSplit(train=train, validation=validation, test=test)


def fit_train_only_scaler(split: ChronologicalSplit) -> tuple[ChronologicalSplit, StandardScaler]:
    """Fit a scaler on train only, then transform validation and test."""
    scaler = StandardScaler()
    train = scaler.fit_transform(split.train)
    validation = scaler.transform(split.validation)
    test = scaler.transform(split.test)
    return ChronologicalSplit(train=train, validation=validation, test=test), scaler


def make_sliding_windows(series: np.ndarray, input_window: int = 48, horizon: int = 24) -> Tuple[np.ndarray, np.ndarray]:
    """Create sliding windows using past observations only."""
    if series.ndim == 1:
        series = series.reshape(-1, 1)
    xs, ys = [], []
    max_start = len(series) - input_window - horizon + 1
    if max_start <= 0:
        raise ValueError("Series is too short for the requested input window and horizon.")
    for i in range(max_start):
        xs.append(series[i:i + input_window])
        ys.append(series[i + input_window:i + input_window + horizon])
    return np.asarray(xs), np.asarray(ys)
