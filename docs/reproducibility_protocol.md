# Reproducibility Protocol

This document summarizes the protocol to be followed by the benchmark notebook.

## Datasets

The reported benchmark uses six real-world datasets: Energy, AAPL log-returns, Jena Climate, ETTh1, ETTm2, and Exchange Rate.

## Preprocessing

1. Load the real dataset.
2. Sort observations chronologically.
3. Apply dataset-specific cleaning and transformation.
4. Split chronologically into 70% train, 15% validation, and 15% test.
5. Fit scalers on the training split only.
6. Apply fitted scalers to validation and test splits.
7. Construct sliding windows using past observations only.

## Forecasting task

- Input window: 48 steps.
- Horizon: 24 steps.

## Repeated runs

Trainable models are evaluated using the following seeds:

```text
42, 123, 2024, 7, 99
```

## Metrics

Primary forecasting metric: MASE.

Supporting metrics: MAE, RMSE, R2, sMAPE, WAPE, Directional Accuracy.

Efficiency metrics: training time, inference latency, parameter count.

Functional-emulation metrics: Pearson correlation with QELM outputs, distributional divergence, spectral distance, autocorrelation-profile distance, and observable-level errors.
