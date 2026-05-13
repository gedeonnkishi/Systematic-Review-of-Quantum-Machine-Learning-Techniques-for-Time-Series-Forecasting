# GitHub upload instructions

## Recommended repository name

`Systematic-Review-of-Quantum-Machine-Learning-Techniques-for-Time-Series-Forecasting`

## Upload using Git

```bash
git init
git add .
git commit -m "Add reproducibility package for QML-TSF CeNN benchmark"
git branch -M main
git remote add origin https://github.com/gedeonnkishi/Systematic-Review-of-Quantum-Machine-Learning-Techniques-for-Time-Series-Forecasting.git
git push -u origin main
```

## Pre-submission checklist

1. Confirm that the GitHub repository is public.
2. Confirm that `README.md` renders correctly.
3. Confirm that the key CSV files are visible under `outputs/full_run/`.
4. Confirm that `notebooks/reproduce_results_from_outputs.ipynb` opens correctly.
5. Replace the benchmark scaffold notebook with the original Kaggle/Colab notebook if it is available.
6. Keep the repository link as a raw URL in the manuscript and in the response to reviewers.
