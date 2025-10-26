# Historical Temperature Trend Analysis for Malawi (1950–2100)

This project analyzes long-term **temperature trends in Malawi** using both historical observations and future climate projections.  
It investigates how mean annual temperatures have evolved between **1950–2014** and estimates future trends up to **2100** using regression modeling and compares the findings .

---

## Project Overview

- **Objective:** Detect and interpret Malawi’s temperature trends using historical model data and modeled future climate datasets.  
- **Scope:** 1950–2100  
- **Focus Variable:** Mean Annual Temperature  
- **Key Tasks:**
  - Data cleaning and transformation  
  - Mann–Kendall trend test and Sen’s slope estimation  
  - Linear regression-based prediction (2015–2100)  
  - Comparison with MIROC6 CMIP6 model (SSP245 scenario)  
  - Visualization and interpretation of temperature dynamics  

---

## Methods and Tools

| Task | Tools / Methods |
|------|------------------|
| Data Processing | Python (Pandas, NumPy) |
| Trend Detection | Mann–Kendall Test, Sen’s Slope Estimator |
| Regression Modeling | Statsmodels (OLS) |
| Visualization | Matplotlib, Seaborn |
| Model Comparison | Pearson Correlation (Default for Pandas) |

---

## Key Findings

- A **statistically significant warming trend** was observed from 1950–2014.  
- **Sen’s slope** indicated a consistent rise in mean annual temperatures.  
- Regression modeling projected a **continued warming pattern** toward 2100.  
- The **Pearson correlation coefficient** between the predicted and MIROC6 model temperatures was approximately **0.73 (p < 0.001)**, showing a **strong, statistically significant positive relationship**.

---

## Personal Reflection

Working on this project allowed me to combine statistical methods with climate science to understand how Malawi’s temperature has changed over time.  
Through the analysis, I improved my ability to handle, analyze, and visualize large datasets while applying robust statistical techniques.  

The experience reinforced my appreciation for **data-driven climate research** and how such insights can guide adaptation strategies in response to rising temperatures and increasing climate variability in Malawi.

## Future Work

- Extending the model to include *precipitation and additional climate variables*.
- Performing ensemble comparisons by integrating outputs from *multiple CMIP6 models*.
- Quantifying and correcting *uncertainty and bias* between predicted and modeled outputs.

---

## Repository Structure
- data
- figures
- notebooks
- scripts
- README
- requirements



## Requirements
See `requirements.txt` (pandas, numpy, matplotlib, pymannkendall, statsmodels...).

## Outputs
- Figures are saved to `figures/`.
- Generated data saved to `data/processed/` as CSV.

## Data Source

**Historical Data (1950–2014):**  
World Bank. (n.d.). *CMIP6 MIROC6 historical mean temperature data for Malawi (1950–2014)*. Retrieved October 26, 2025, from [https://cckpapi.worldbank.org/api/v1/cmip6-x0.25_timeseries_tas_timeseries_annual_1950-2014_mean_historical_miroc6_r1i1p1f1_mean/MWI?_format=json](https://cckpapi.worldbank.org/api/v1/cmip6-x0.25_timeseries_tas_timeseries_annual_1950-2014_mean_historical_miroc6_r1i1p1f1_mean/MWI?_format=json)

**Future Projections (2015–2100, SSP2-4.5):**  
World Bank. (n.d.). *CMIP6 MIROC6 mean temperature projections for Malawi under SSP2-4.5 (2015–2100)*. Retrieved October 26, 2025, from [https://cckpapi.worldbank.org/api/v1/cmip6-x0.25_timeseries_tas_timeseries_annual_2015-2100_mean_ssp245_miroc6_r1i1p1f1_mean/MWI?_format=json](https://cckpapi.worldbank.org/api/v1/cmip6-x0.25_timeseries_tas_timeseries_annual_2015-2100_mean_ssp245_miroc6_r1i1p1f1_mean/MWI?_format=json)




## Produced By:

Jimmy Jay-Jay (Jimmy Edward Matewere) 
- LinkedIn: [jimmy-matewere-59a116367](https://www.linkedin.com/in/jimmy-matewere-59a116367)
- Email: jmatewere265@gmail.com
