# Mapping Heart Health  
### County-Level Behavioral Risk Factors and Heart Disease Mortality

**Author:** J. Casey Brookshier  
**Date:** July 31, 2025  

---

## Project Overview

This project examines whether U.S. counties with higher levels of key behavioral
risk factors—**smoking, obesity, and physical inactivity**—experience higher
**age-adjusted heart disease mortality rates**.

Using publicly available health datasets, the analysis demonstrates an
end-to-end analytical workflow, from data preparation through statistical
modeling and interpretation.

---

## Research Question

> Do counties with higher rates of behavioral risk factors have significantly
> higher heart disease mortality?

---

## Data Sources

- **CDC WONDER** (2018–2020)  
  Age-adjusted heart disease mortality rates at the county level
- **County Health Rankings** (2019)  
  Behavioral risk factor prevalence (smoking, obesity, physical inactivity)
- **USDA Rural–Urban Continuum Codes** (2023)  
  County-level rural–urban classification

All datasets were cleaned and merged using standardized **5-digit FIPS codes**.

---

## Methods

- Data cleaning and harmonization
- Exploratory correlation analysis (Pearson r)
- Visualization with regression overlays
- Ordinary Least Squares (OLS) regression
  - Univariate models
  - Multivariate model including all risk factors

---

## Key Findings

- All three behavioral risk factors are **positively and statistically significantly**
  associated with heart disease mortality.
- **Physical inactivity** and **smoking** show the strongest relationships.
- The multivariate model explains approximately **17% of the variance** in
  county-level mortality rates.

---

## Limitations

- Ecological (county-level) analysis
- Spatial autocorrelation not explicitly modeled
- Omitted variables such as healthcare access, income, and environmental factors

---

## Repository Structure
mapping-heart-health/
├── README.md
├── requirements.txt
├── data/
│ └── merged_heart_health_data.csv
├── notebooks/
│ └── heart_disease_behavioral_risk_analysis.ipynb
└── plots/
├── scatter_behavioral_risk.png
└── correlation_heatmap.png

HOW TO RUN


## How to Run
```bash
git clone git@github.com:CrassSax7/Analyzing-US-Census-Public-Health.git
cd Analyzing-US-Census-Public-Health
pip install -r requirements.txt
python scripts/analysis.py

