# Quantum-Inspired Time Series Forecasting: CeNN Functional Emulation Benchmark

This repository provides a reproducibility-oriented implementation package for the revised manuscript:

**Quantum-Inspired Time Series Forecasting: A Systematic Review and Neuro-Symbolic Emulation Framework**

The repository supports the bounded proof-of-concept benchmark reported in the revised manuscript. It includes the notebook workflow, experiment outputs, result tables, figures, logs, model checkpoints, and configuration files used to evaluate a neuro-symbolic Cellular Neural Network (CeNN)-based functional emulator for time-series forecasting.

The goal of this repository is **controlled reproducibility**, not production deployment or proof of physical quantum advantage.

---

## 1. Repository Purpose

This repository is intended to help reviewers and researchers:

- inspect the implementation of the CeNN-based proof-of-concept benchmark;
- reproduce the main experimental workflow in a Kaggle notebook environment;
- verify the reported datasets, preprocessing protocol, random seeds, hyperparameters, and metrics;
- access the generated tables, figures, logs, statistical tests, and ablation outputs used in the revised manuscript.

The repository should be understood as a **research reproducibility package** accompanying a revised IEEE Access submission.

---

## 2. Scientific Scope and Limitations

The proposed CeNN framework is a **classical quantum-inspired functional emulator**. It is not a quantum computer and does not simulate full quantum states.

The framework does **not** claim:

- physical quantum computation;
- genuine quantum entanglement reproduction;
- exact quantum-state simulation;
- quantum computational advantage;
- universal superiority over classical forecasting models;
- industrial readiness.

Instead, the benchmark evaluates whether a locally connected CeNN emulator can provide competitive forecasting performance under a controlled protocol while preserving favorable memory-scaling assumptions.

The revised results are **domain-dependent**:

- CeNN obtains the best MAPE on the energy dataset.
- CeNN remains competitive but is not uniformly superior on AAPL, Jena Climate, and Mackey--Glass.
- Classical neural baselines outperform CeNN on some datasets.

---

## 3. Experimental Protocol

The proof-of-concept benchmark uses the following fixed protocol:

| Item | Protocol |
|---|---|
| Evaluation type | Bounded proof-of-concept benchmark |
| Number of datasets | 4 |
| Observations per dataset | 6000 chronological observations |
| Split | 70% train, 15% validation, 15% test |
| Forecasting horizon | One-step-ahead forecasting |
| Input window length | 24 past observations |
| Runs | 5 seeds for trainable models |
| Seeds | 42, 43, 44, 45, 46 |
| Main metrics | MAE, RMSE, MAPE, sMAPE, R² |
| Computational metrics | Training time and inference latency |
| Main execution environment | Kaggle notebook environment |
| GPU used | NVIDIA Tesla T4 |

The split is strictly chronological. No random shuffling is used for time-series splitting.

Normalization parameters are fitted on the training split only and then applied to validation and test splits to prevent lookahead leakage.

---

## 4. Datasets

The notebook loads or generates the datasets used in the revised benchmark.

| Dataset | Domain | Source / Loading Mode | Target Variable | Fallback Used |
|---|---|---|---|---|
| Energy | Energy load forecasting | Kaggle dataset: `robikscube/hourly-energy-consumption`, file `PJME_hourly.csv` | `PJME_MW` | No |
| AAPL | Financial forecasting | Kaggle dataset: `meetnagadia/apple-stock-price-from-19802021`, file `AAPL.csv` | `Adj Close` | No |
| Jena Climate | Weather forecasting | Kaggle dataset: `mnassrib/jena-climate`, file `jena_climate_2009_2016.csv` | `T (degC)` | No |
| Mackey--Glass | Chaotic deterministic benchmark | Deterministic generator included in the notebook | `x(t)` | No |

### Important note on fallback logic

The notebook may contain a fallback option for pipeline testing. However, the reported benchmark did **not** use synthetic fallback datasets.

The final audit confirms:

```text
any_synthetic_fallback = false
```

The fallback logic exists only to prevent pipeline failure during testing and should not be interpreted as part of the reported experimental results.

---

## 5. Models Compared

The benchmark evaluates the following model families:

1. **Seasonal Naive**
2. **ARIMA**
3. **MLP**
4. **LSTM**
5. **TransformerEncoder**
6. **CeNN emulator**

Seasonal Naive and ARIMA are treated as deterministic or single-run baselines. Neural models and the CeNN emulator are evaluated over five independent random seeds.

---

## 6. Main Hyperparameters

| Hyperparameter | Value |
|---|---|
| Optimizer | Adam |
| Learning rate | `1e-3` |
| Weight decay | `1e-5` |
| Batch size | 64 |
| Maximum epochs | 50 |
| Early stopping patience | 8 epochs |
| Gradient clipping | `max_norm = 1.0` |
| MLP hidden size | 128 |
| LSTM hidden size | 64 |
| Transformer dimension | `d_model = 64` |
| Transformer heads | 4 |
| Transformer layers | 2 |
| CeNN cells | 64 |
| CeNN local radius | 2 |
| CeNN neighbors per cell | 5 |
| CeNN integration steps | 6 |
| CeNN integration step | `Δt = 0.15` |
| CeNN topology | 1D ring neighborhood |

---

## 7. Software Environment

The reported experiments were executed under the following environment:

| Component | Version / Configuration |
|---|---|
| Platform | Kaggle notebook environment |
| GPU | NVIDIA Tesla T4 |
| Python | 3.12.12 |
| PyTorch | 2.10.0+cu128 |
| NumPy | 2.0.2 |
| Pandas | 2.3.3 |

A `requirements.txt` file is provided for transparency and controlled replication outside the original Kaggle session.

Because cloud notebook environments may vary across sessions, exact bitwise reproduction is not guaranteed. The objective is reproducibility within reasonable numerical tolerance.

---

## 8. Recommended Repository Structure

The recommended structure is:

```text
repository/
├── README.md
├── requirements.txt
├── CeNN_QML_TSF_Revision_Benchmark.ipynb
├── outputs_revision_package.zip
└── outputs_revision/
    ├── configs/
    ├── logs/
    ├── models/
    ├── results/
    ├── figures/
    └── tables/
```

If possible, keep both:

1. the compressed archive `outputs_revision_package.zip`;
2. the extracted `outputs_revision/` folder.

This makes the repository easier to inspect without requiring reviewers to download and manually explore the ZIP file first.

---

## 9. Output Package Contents

The current output package is organized as follows:

```text
outputs_revision/
├── configs/
│   └── experiment_config.json
│
├── logs/
│   ├── environment_info.json
│   └── final_audit.json
│
├── models/
│   └── checkpoints/
│
├── results/
│   ├── all_runs_metrics.csv
│   ├── summary_mean_std.csv
│   ├── statistical_tests.csv
│   ├── statistical_tests_runlevel.csv
│   ├── statistical_tests_pointlevel.csv
│   ├── ablation_all_runs.csv
│   ├── ablation_summary.csv
│   ├── dataset_metadata.csv
│   ├── split_summary.csv
│   ├── test_predictions.csv
│   └── training_histories.csv
│
├── figures/
│   ├── actual_vs_predicted_energy_CeNN.png
│   ├── actual_vs_predicted_aapl_CeNN.png
│   ├── actual_vs_predicted_jena_climate_CeNN.png
│   ├── actual_vs_predicted_mackey_glass_CeNN.png
│   ├── mape_comparison_all_datasets.png
│   ├── latency_comparison_all_datasets.png
│   └── training_loss_*.png
│
└── tables/
    ├── table_main_results.tex
    ├── table_main_results.csv
    ├── table_statistical_validation.tex
    ├── table_statistical_validation_runlevel.tex
    ├── table_statistical_validation_pointlevel.tex
    ├── table_ablation.tex
    ├── table_environment.tex
    ├── table_environment.csv
    ├── table_hyperparameters.tex
    ├── table_hyperparameters.csv
    ├── table_experimental_protocol.tex
    └── table_experimental_protocol.csv
```

---

## 10. How to Run the Benchmark

### Option A: Run on Kaggle

This is the recommended execution mode because the reported experiments were run in a Kaggle notebook environment.

1. Create a new Kaggle notebook.
2. Attach the required Kaggle datasets:
   - `robikscube/hourly-energy-consumption`
   - `meetnagadia/apple-stock-price-from-19802021`
   - `mnassrib/jena-climate`
3. Upload or open the notebook:
   - `CeNN_QML_TSF_Revision_Benchmark.ipynb`
4. Enable GPU acceleration.
5. Run all cells from top to bottom.
6. Check the generated outputs under `outputs_revision/`.

### Option B: Run locally

Local execution is possible if the required datasets are available and the environment is compatible.

Install dependencies:

```bash
pip install -r requirements.txt
```

Then run the notebook using Jupyter:

```bash
jupyter notebook CeNN_QML_TSF_Revision_Benchmark.ipynb
```

Local execution may require adapting dataset paths.

---

## 11. Key Result Files

The most important files for verification are:

| File | Purpose |
|---|---|
| `dataset_metadata.csv` | Dataset sources, target columns, fallback status |
| `split_summary.csv` | Train/validation/test split details |
| `all_runs_metrics.csv` | Metrics for all datasets, models, and seeds |
| `summary_mean_std.csv` | Mean and standard deviation summary |
| `statistical_tests_runlevel.csv` | Run-level statistical tests |
| `statistical_tests_pointlevel.csv` | Point-level statistical tests |
| `ablation_summary.csv` | Ablation results summary |
| `environment_info.json` | Software and hardware metadata |
| `final_audit.json` | Final audit of experiment consistency |
| `test_predictions.csv` | Test-set predictions |
| `training_histories.csv` | Training losses and validation histories |

---

## 12. Main Result Summary

The revised benchmark reports the following CeNN MAPE values:

| Dataset | CeNN MAPE |
|---|---|
| Energy | `1.6879 ± 0.0685` |
| AAPL | `2.7541 ± 0.4315` |
| Jena Climate | `4.3628 ± 0.2201` |
| Mackey--Glass | `0.1866 ± 0.0127` |

These values should be interpreted as proof-of-concept results under the fixed protocol described above.

---

## 13. Reproducibility Boundaries

The following limitations should be considered:

- Results may vary slightly across hardware, CUDA versions, and cloud sessions.
- Timing and latency results are environment-specific.
- The benchmark uses 6000 chronological observations per dataset, not complete full-dataset training.
- The forecasting horizon is one step ahead.
- The CeNN emulator is classical and does not implement physical quantum computation.
- The reported evidence supports feasibility and competitiveness in selected settings, not universal superiority.

---

## 14. Citation

If this repository supports your work, please cite the associated manuscript once bibliographic information is available.

Suggested citation placeholder:

```bibtex
@article{nkishi2026qmltsf,
  title   = {Quantum-Inspired Time Series Forecasting: A Systematic Review and Neuro-Symbolic Emulation Framework},
  author  = {Nkishi Djenga, Gedeon and Kambale, Witesyavwirwa Vianney and Kambale, Exauce Maruba and Bisuta, Hughes Bieto and Kyamakya, Kyandoghere},
  journal = {IEEE Access},
  year    = {2026},
  note    = {Under review}
}
```

---

## 15. License

Add the selected license file at the repository root.

Recommended options:

- MIT License for code;
- CC BY 4.0 for documentation and figures, if appropriate.

Choose only licenses that are compatible with the manuscript, dataset licenses, and institutional requirements.

---

## 16. Contact

For questions about the repository or the manuscript, contact the corresponding author listed in the revised manuscript.

---

## 17. Reviewer-Oriented Note

This repository was organized to address reproducibility concerns raised during peer review, especially regarding:

- missing implementation details;
- missing hyperparameters;
- limited reproducibility information;
- unclear dataset processing;
- lack of statistical validation;
- limited visibility of generated outputs.

The repository therefore exposes the notebook workflow, experiment configuration, generated outputs, statistical tests, figures, tables, and environment metadata used in the revised manuscript.
