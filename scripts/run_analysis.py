"""
Mapping Heart Health

"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import pearsonr


# Paths (define path relative to repo root for repo portability)
# define plots directory, create if it doesn't exist

DATA_PATH = os.path.join("data", "merged_heart_health_data.csv")
PLOTS_DIR = os.path.join("plots")
os.makedirs(PLOTS_DIR, exist_ok=True)


# Load data -> csv into df, fips read as string 
# (preserve leading zeros), select only analysis important 
# columns, remove rows lacking missing values

df = pd.read_csv(DATA_PATH, dtype={"fips": str})

df = df[
    [
        "mortality_rate",
        "smoking_rate",
        "obesity_rate",
        "inactivity_rate"
    ]
].dropna()

print(f"Loaded dataset with {df.shape[0]:,} county observations")


# Correlation analysis -> Iterate over risk factor var, compute
# pearson correlation coef, p-value (linear assoc w/ mortality)

print("\n=== Pearson Correlations with Mortality Rate ===")
for var in ["smoking_rate", "obesity_rate", "inactivity_rate"]:
    r, p = pearsonr(df[var], df["mortality_rate"])
    print(f"{var}: r = {r:.3f}, p < 0.001")


# Multivariate regression -> define dependent/independent var, add 
# intercept, fit ordinary least squares regression model (estimate
# independent effect of each risk factor, print stat summary

X = df[["smoking_rate", "obesity_rate", "inactivity_rate"]]
X = sm.add_constant(X)
y = df["mortality_rate"]

model = sm.OLS(y, X).fit()
print("\n=== Multivariate OLS Regression ===")
print(model.summary())


# Scatter plots with regression -> set default plot style, 
# fitted regression line for dependent var

sns.set(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.regplot(
    data=df,
    x="smoking_rate",
    y="mortality_rate",
    scatter_kws={"alpha": 0.3},
    ax=axes[0]
)
axes[0].set_title("Smoking Rate vs Heart Disease Mortality")

sns.regplot(
    data=df,
    x="obesity_rate",
    y="mortality_rate",
    scatter_kws={"alpha": 0.3},
    ax=axes[1]
)
axes[1].set_title("Obesity Rate vs Heart Disease Mortality")

sns.regplot(
    data=df,
    x="inactivity_rate",
    y="mortality_rate",
    scatter_kws={"alpha": 0.3},
    ax=axes[2]
)
axes[2].set_title("Physical Inactivity vs Heart Disease Mortality")

plt.tight_layout()
plt.savefig(
    os.path.join(PLOTS_DIR, "scatter_behavioral_risk.png"),
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# Correlation heatmap -> compute correlation matrix for 
# selected var

corr = df.corr()

plt.figure(figsize=(5, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix: Behavioral Risk Factors")

plt.tight_layout()
plt.savefig(
    os.path.join(PLOTS_DIR, "correlation_heatmap.png"),
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("\nAnalysis complete.")
print(f"Plots saved to '{PLOTS_DIR}/'")