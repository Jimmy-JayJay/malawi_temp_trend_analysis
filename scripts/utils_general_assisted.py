# scripts/utils.py
"""
Utility functions for Malawi climate trend analysis.
Handles data loading, QC, and small plotting utilities.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

# --------------------------------------------------------
# File management utilities
# --------------------------------------------------------

def ensure_dir(path: Path):
    """Create directory if it doesn’t exist."""
    path.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------------
# Data loading and date detection
# --------------------------------------------------------

def load_and_parse_csv(file_path: Path) -> pd.DataFrame:
    """
    Load a CSV and try to automatically detect the date column.
    Returns a DataFrame with a standardized 'date' column.
    """
    df = pd.read_csv(file_path)

    # Find date-like column
    date_col = None
    for col in df.columns:
        if col.lower() in ['date', 'datetime', 'time', 'timestamp']:
            date_col = col
            break

    # Infer from first column if not found
    if date_col is None:
        first_col = df.columns[0]
        parsed = pd.to_datetime(df[first_col], errors='coerce', infer_datetime_format=True)
        if parsed.notna().sum() / len(parsed) > 0.8:
            date_col = first_col

    # Melt wide-format tables if necessary
    if date_col is None:
        id_vars = [c for c in df.columns if df[c].dtype == object]
        if len(id_vars) == 0:
            id_vars = [df.columns[0]]
        value_vars = [c for c in df.columns if c not in id_vars]

        df = df.melt(id_vars=id_vars, value_vars=value_vars,
                     var_name='date', value_name='temp_mean')

        df['date'] = pd.to_datetime(df['date'], errors='coerce', infer_datetime_format=True)
        df = df.dropna(subset=['date', 'temp_mean']).reset_index(drop=True)
        date_col = 'date'

    # Parse date column and rename
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce', infer_datetime_format=True)
    if date_col != 'date':
        df = df.rename(columns={date_col: 'date'})

    df.sort_values('date', inplace=True)
    return df


# --------------------------------------------------------
# Data quality checks
# --------------------------------------------------------

def flag_outliers(series: pd.Series, lower: float, upper: float) -> pd.Series:
    """Flag values outside a plausible range."""
    return (series < lower) | (series > upper)


def interpolate_gaps(series: pd.Series, limit=3) -> pd.Series:
    """Linearly interpolate small missing gaps."""
    return series.interpolate(method='linear', limit=limit)


# --------------------------------------------------------
# Plot utilities
# --------------------------------------------------------

def plot_qc(original_df: pd.DataFrame, clean_df: pd.DataFrame, date_col='date', value_col='temp_mean'):
    """Plot before/after interpolation comparison."""
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(original_df[date_col], original_df[value_col], color='steelblue', label='Original')
    ax.plot(clean_df[date_col], clean_df[value_col], color='orange', label='Interpolated')
    ax.set_title('Temperature QC Check')
    ax.set_xlabel('Date')
    ax.set_ylabel('Mean Temperature (°C)')
    ax.legend()
    plt.show()