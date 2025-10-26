## Malawi Climate Trends — Temperature & Precipitation


This repository contains the analysis for historical mean temperature  trends in Malawi. The analysis includes QC, exploration, anomaly calculation, trend detection (Mann–Kendall & Sen's slope), and visualization.


## Structure
- `data/raw/` — original downloaded data (do not modify)
- `data/processed/` — cleaned data ready for analysis and data exports
- `notebooks/` — Jupyter notebooks for each analysis step
- `scripts/` — utility scripts used by notebooks
- `figures/` — generated figures
- `results/` — tables of trend statistics


## Quick start
1. Create and activate venv (see requirements below).
2. Place your CSV (`mean_historical_temp.csv`) in `data/raw/`.
3. Run `notebooks/01_data_qc.ipynb` to produce a cleaned `data/processed/` file.
4. Continue with EDA and trend notebooks.


## Requirements
See `requirements.txt` (pandas, numpy, matplotlib, xarray, pymannkendall, statsmodels...).


## Outputs
- Figures are saved to `figures/`.
- Computed statistics saved to `results/` as CSV.
- Generated data saved to `data/processed/` as CSV


## Author
Jimmy Jay-Jay (Jimmy Edward Matewere) — contact: (jmatewere265@gmail.com)