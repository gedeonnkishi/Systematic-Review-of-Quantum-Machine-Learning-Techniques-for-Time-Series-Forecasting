# Reproducibility protocol

## Published full-run protocol

The reported benchmark uses:

- up to 20,000 chronological observations per dataset;
- 70/15/15 chronological train/validation/test split;
- input window length = 48;
- forecast horizon = 24;
- five random seeds: 42, 123, 2024, 7, 99;
- primary forecasting metric: MASE;
- supporting metrics: MAE, RMSE, R²;
- emulation metrics: Pearson r, KL divergence, spectral distance, autocorrelation distance, observable-feature MSE;
- scalability cells: 16, 32, 64, 128, 256, 512.

## Important boundary

The repository is designed for controlled replication, not bitwise-identical reproduction. Cloud GPU allocation, CUDA kernels, PyTorch versions, and data-loader behavior can introduce small numerical differences even under fixed seeds.

## How to verify results without rerunning the full notebook

The published outputs are available in `outputs/`:

- `summary_full.csv`
- `benchmark_full.csv`
- `emulation_summary_full.csv`
- `emulation_fidelity_full.csv`
- `ablation_full.csv`
- `scalability_full.csv`
- `linear_fit_full.csv`
- `statistical_comparison_full.csv`
- `metadata_full.json`

These files are sufficient to inspect the reported tables, figures, and main conclusions.

## How to rerun

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Place datasets in `data/` as described in `data/README.md`.

3. Open the notebook:

```bash
jupyter notebook notebooks/neurosymbolic-cenn-qml-tsf-benchmark.ipynb
```

4. Use `RUN_MODE = 'smoke'` for a quick pipeline check or `RUN_MODE = 'full'` for the reported full-run protocol.

## Expected output directory

The notebook writes results to:

```text
outputs_v11_2_final_fullrun_ready/
```

For the public repository, the exported full-run files are stored in:

```text
outputs/
figures/
```
