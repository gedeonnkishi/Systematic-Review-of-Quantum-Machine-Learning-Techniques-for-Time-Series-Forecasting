"""Forecasting and functional-emulation metrics."""

from __future__ import annotations

import numpy as np
from scipy.stats import pearsonr


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(np.abs(y_true - y_pred)))


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def mase(y_true: np.ndarray, y_pred: np.ndarray, y_train: np.ndarray, seasonality: int = 1) -> float:
    """Mean Absolute Scaled Error.

    The denominator is computed from the training series only.
    """
    y_true = np.asarray(y_true).reshape(-1)
    y_pred = np.asarray(y_pred).reshape(-1)
    y_train = np.asarray(y_train).reshape(-1)
    if len(y_train) <= seasonality:
        raise ValueError("Training series is too short for the requested seasonality.")
    denom = np.mean(np.abs(y_train[seasonality:] - y_train[:-seasonality]))
    if denom == 0:
        return float("inf")
    return float(np.mean(np.abs(y_true - y_pred)) / denom)


def smape(y_true: np.ndarray, y_pred: np.ndarray, eps: float = 1e-8) -> float:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return float(100 * np.mean(2 * np.abs(y_pred - y_true) / (np.abs(y_true) + np.abs(y_pred) + eps)))


def wape(y_true: np.ndarray, y_pred: np.ndarray, eps: float = 1e-8) -> float:
    return float(np.sum(np.abs(y_true - y_pred)) / (np.sum(np.abs(y_true)) + eps))


def directional_accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    y_true = np.asarray(y_true).reshape(-1)
    y_pred = np.asarray(y_pred).reshape(-1)
    if len(y_true) < 2:
        return float("nan")
    return float(np.mean(np.sign(np.diff(y_true)) == np.sign(np.diff(y_pred))))


def pearson_alignment(reference: np.ndarray, candidate: np.ndarray) -> float:
    ref = np.asarray(reference).reshape(-1)
    cand = np.asarray(candidate).reshape(-1)
    if np.std(ref) == 0 or np.std(cand) == 0:
        return float("nan")
    return float(pearsonr(ref, cand).statistic)


def autocorrelation_profile(x: np.ndarray, max_lag: int = 24) -> np.ndarray:
    x = np.asarray(x).reshape(-1)
    x = x - np.mean(x)
    denom = np.dot(x, x)
    if denom == 0:
        return np.zeros(max_lag)
    return np.array([np.dot(x[:-lag], x[lag:]) / denom for lag in range(1, max_lag + 1)])


def autocorrelation_distance(reference: np.ndarray, candidate: np.ndarray, max_lag: int = 24) -> float:
    return float(np.linalg.norm(autocorrelation_profile(reference, max_lag) - autocorrelation_profile(candidate, max_lag)))


def spectral_distance(reference: np.ndarray, candidate: np.ndarray) -> float:
    ref = np.abs(np.fft.rfft(np.asarray(reference).reshape(-1)))
    cand = np.abs(np.fft.rfft(np.asarray(candidate).reshape(-1)))
    ref = ref / (np.linalg.norm(ref) + 1e-12)
    cand = cand / (np.linalg.norm(cand) + 1e-12)
    return float(np.linalg.norm(ref - cand))
