# Quantum-Inspired Time Series Forecasting: Neuro-Symbolic CeNN Functional Emulation Benchmark

This repository contains the reproducibility package for the proof-of-concept benchmark associated with the manuscript:

**Quantum-Inspired Time Series Forecasting: A Systematic Review and Neuro-Symbolic Emulation Framework**

The repository evaluates whether a classical **neuro-symbolic Cellular Neural Network (CeNN)** can act as a bounded functional emulator of selected behaviors of a **Quantum Extreme Learning Machine (QELM)** reference model for time series forecasting.

## Scientific scope

This project does **not** claim that CeNN is a quantum computer, a physical quantum-state simulator, or evidence of quantum computational advantage. The goal is narrower and explicitly methodological:

- study QML limitations for time series forecasting;
- use QELM as a measurable quantum-inspired teacher;
- evaluate CeNN as a classical functional emulator;
- measure forecasting utility, QELM alignment, ablation behavior, and architectural scalability;
- provide reproducible outputs for reviewer inspection.

## Main benchmark protocol

| Item | Protocol |
|---|---|
| Datasets | Energy, AAPL log-returns, Jena Climate, Mackey--Glass |
| Observations | Up to 20,000 chronological observations per dataset |
| Split | 70/15/15 chronological train/validation/test split |
| Input window | 48 past observations |
| Forecast horizon | 24 steps |
| Seeds | 42, 123, 2024, 7, 99 |
| Primary metric | MASE |
| Supporting metrics | MAE, RMSE, R² |
| Emulation metrics | Pearson r, KL divergence, spectral distance, autocorrelation distance, feature MSE |
| Baselines | Persistence, moving average, MLP, LSTM, Transformer, QELM teacher |
| CeNN variants | `CeNN_NS`, `CeNN_Emulator` |

## Repository structure

```text
.
├── notebooks/      # Main reproducibility notebook
├── outputs/        # Published full-run CSV, JSON, and figure outputs
├── figures/        # Manuscript/GitHub-ready figures
├── data/           # Dataset placement instructions; raw data are not redistributed
├── paper/          # Manuscript PDF snapshot
├── README.md
├── REPRODUCIBILITY.md
├── requirements.txt
├── CITATION.cff
└── LICENSE
```

## Quick start

Install dependencies:

```bash
pip install -r requirements.txt
```

Open the notebook:

```bash
jupyter notebook notebooks/neurosymbolic-cenn-qml-tsf-benchmark.ipynb
```

Use:

```python
RUN_MODE = 'smoke'
```

for a quick pipeline check, or:

```python
RUN_MODE = 'full'
```

for the full benchmark protocol reported in the manuscript.

## Data

Raw third-party datasets are not redistributed by default. See [`data/README.md`](data/README.md) for the expected local filenames and columns.

Expected files:

- `data/powerconsumption.csv`
- `data/aapl.csv`
- `data/jena_climate.csv`

The Mackey--Glass chaotic series is generated internally by the notebook.

The reported manuscript results correspond to the exported full-run files in [`outputs/`](outputs/), not to diagnostic fallback data.

## Key outputs

The main exported result files are:

| File | Role |
|---|---|
| `summary_full.csv` | Aggregated performance by dataset and model |
| `benchmark_full.csv` | Seed-level forecasting results |
| `emulation_summary_full.csv` | Functional emulation summary |
| `emulation_fidelity_full.csv` | Detailed emulation metrics |
| `ablation_full.csv` | Ablation study results |
| `scalability_full.csv` | Scalability measurements |
| `linear_fit_full.csv` | Linear fit diagnostics for scalability |
| `statistical_comparison_full.csv` | Statistical comparisons |
| `metadata_full.json` | Run configuration and environment metadata |

## Main figures

| Figure | File |
|---|---|
| CeNN/QELM architecture | `figures/architecture_overview.png` |
| MASE benchmark heatmap | `figures/benchmark_mase_heatmap.png` |
| Functional emulation comparison | `figures/emulation_model_comparison.png` |
| Scalability analysis | `figures/scalability.png` |
| Ablation overview | `figures/ablation_overview.png` |
| Teacher selection diagnostics | `figures/teacher_selection.png` |
| Extended diagnostics | `figures/main_results.png` |

## Summary of reported findings

The full-run results support a bounded conclusion:

- `CeNN_NS` is competitive but not uniformly superior to MLP or LSTM.
- Functional emulation is strongest on the Mackey--Glass benchmark.
- Energy and Jena show weaker but measurable QELM alignment.
- AAPL log-returns are treated cautiously because naive and QELM outputs are near-degenerate under the selected transformation.
- Parameter growth supports near-linear architectural scaling, while runtime and latency remain hardware-sensitive.
- Ablations show a trade-off between direct forecasting accuracy and QELM functional alignment.

## Reproducibility boundary

This repository is intended for transparent inspection and controlled replication. It does not guarantee bitwise-identical reproduction across all systems, because cloud GPU allocation, PyTorch/CUDA versions, and floating-point scheduling can introduce small numerical differences.

## Citation

Please cite the associated manuscript and this repository if you use the code, outputs, or figures. A machine-readable citation file is provided in [`CITATION.cff`](CITATION.cff).

## License

The code and documentation are released under the MIT License. Third-party datasets remain governed by their original licenses.
