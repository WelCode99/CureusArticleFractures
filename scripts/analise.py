import pandas as pd

# Read the CSV file
# The path "../dados/" suggests the "data" folder is one level above the script's location.
# This is translated to "../data/" to match the English repository structure.
df = pd.read_csv("../data/FraturasCorrigido.csv")

# Display basic information about the DataFrame
print("Initial DataFrame information:")
df.info()

# Display the first 5 rows of the DataFrame
print("\nFirst 5 rows of the DataFrame:")
print(df.head())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Display descriptive statistics for numerical columns
print("\nDescriptive statistics for numerical columns:")
print(df.describe())

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Drop completely null columns
df = df.drop(columns=["DIAGSEC8", "DIAGSEC9"])

# Convert date columns to datetime objects
df["DT_INTER"] = pd.to_datetime(df["DT_INTER"])
df["DT_SAIDA"] = pd.to_datetime(df["DT_SAIDA"])

# Calculate days of hospitalization
df["DIAS_INTERNACAO"] = (df["DT_SAIDA"] - df["DT_INTER"]).dt.days

# --- In-depth Descriptive Statistics and Visualization ---

print("\n--- Detailed Statistical Analysis ---")

# 1. Analysis of Categorical Variables

# SEXO (Gender)
print("\nAnalysis of the 'SEXO' Variable:")
sexo_counts = df["SEXO"].value_counts()
sexo_proportions = df["SEXO"].value_counts(normalize=True) * 100
print(pd.DataFrame({"Count": sexo_counts, "Proportion (%)": sexo_proportions}))

plt.figure(figsize=(8, 6))
sns.countplot(x="SEXO", data=df, palette="viridis")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# MORTE (Death)
print("\nAnalysis of the 'MORTE' Variable:")
morte_counts = df["MORTE"].value_counts()
morte_proportions = df["MORTE"].value_counts(normalize=True) * 100
print(pd.DataFrame({"Count": morte_counts, "Proportion (%)": morte_proportions}))

plt.figure(figsize=(8, 6))
sns.countplot(x="MORTE", data=df, palette="plasma")
plt.title("Distribution of Deaths")
plt.xlabel("Death")
plt.ylabel("Count")
plt.show()

# faixa_etaria_corrigida (Corrected Age Group)
print("\nAnalysis of the 'faixa_etaria_corrigida' Variable:")
faixa_etaria_counts = df["faixa_etaria_corrigida"].value_counts().sort_index()
faixa_etaria_proportions = (
    df["faixa_etaria_corrigida"].value_counts(normalize=True).sort_index() * 100
)
print(
    pd.DataFrame(
        {"Count": faixa_etaria_counts, "Proportion (%)": faixa_etaria_proportions}
    )
)

plt.figure(figsize=(12, 7))
sns.countplot(
    y="faixa_etaria_corrigida",
    data=df,
    order=faixa_etaria_counts.index,
    palette="cividis",
)
plt.title("Distribution by Corrected Age Group")
plt.xlabel("Count")
plt.ylabel("Age Group")
plt.show()

# tipo_fratura (Fracture Type)
print("\nAnalysis of the 'tipo_fratura' Variable:")
tipo_fratura_counts = df["tipo_fratura"].value_counts()
tipo_fratura_proportions = df["tipo_fratura"].value_counts(normalize=True) * 100
print(
    pd.DataFrame(
        {"Count": tipo_fratura_counts, "Proportion (%)": tipo_fratura_proportions}
    )
)

plt.figure(figsize=(12, 8))
sns.countplot(
    y="tipo_fratura", data=df, order=tipo_fratura_counts.index, palette="magma"
)
plt.title("Distribution by Fracture Type")
plt.xlabel("Count")
plt.ylabel("Fracture Type")
plt.show()

# regiao (Region)
print("\nAnalysis of the 'regiao' Variable:")
regiao_counts = df["regiao"].value_counts()
regiao_proportions = df["regiao"].value_counts(normalize=True) * 100
print(pd.DataFrame({"Count": regiao_counts, "Proportion (%)": regiao_proportions}))

plt.figure(figsize=(10, 7))
sns.countplot(y="regiao", data=df, order=regiao_counts.index, palette="GnBu_d")
plt.title("Distribution by Fracture Region")
plt.xlabel("Count")
plt.ylabel("Region")
plt.show()

# tem_osteoporose (Has Osteoporosis)
print("\nAnalysis of the 'tem_osteoporose' Variable:")
osteoporose_counts = df["tem_osteoporose"].value_counts()
osteoporose_proportions = df["tem_osteoporose"].value_counts(normalize=True) * 100
print(
    pd.DataFrame(
        {"Count": osteoporose_counts, "Proportion (%)": osteoporose_proportions}
    )
)

# obito_hospitalar (Hospital Death) (rechecking as it was 0 for all)
print("\nAnalysis of the 'obito_hospitalar' Variable:")
obito_hospitalar_counts = df["obito_hospitalar"].value_counts()
obito_hospitalar_proportions = df["obito_hospitalar"].value_counts(normalize=True) * 100
print(
    pd.DataFrame(
        {
            "Count": obito_hospitalar_counts,
            "Proportion (%)": obito_hospitalar_proportions,
        }
    )
)

# ano_internacao (Year of Hospitalization)
print("\nAnalysis of the 'ano_internacao' Variable:")
ano_internacao_counts = df["ano_internacao"].value_counts().sort_index()
ano_internacao_proportions = (
    df["ano_internacao"].value_counts(normalize=True).sort_index() * 100
)
print(
    pd.DataFrame(
        {"Count": ano_internacao_counts, "Proportion (%)": ano_internacao_proportions}
    )
)

plt.figure(figsize=(10, 6))
sns.countplot(x="ano_internacao", data=df, palette="coolwarm")
plt.title("Number of Hospitalizations per Year")
plt.xlabel("Year of Hospitalization")
plt.ylabel("Count")
plt.show()

# 2. Analysis of Numerical Variables

# IDADE (Age)
print("\nAnalysis of the 'IDADE' Variable:")
print(df["IDADE"].describe())
print(f"Skewness (IDADE): {df['IDADE'].skew():.2f}")
print(f"Kurtosis (IDADE): {df['IDADE'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df["IDADE"], kde=True, bins=30, color="skyblue")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
sns.boxplot(y="IDADE", data=df, color="lightcoral")
plt.title("Age Box Plot")
plt.ylabel("Age")
plt.show()

# VAL_TOT (Total Hospitalization Cost)
print("\nAnalysis of the 'VAL_TOT' Variable (Total Hospitalization Cost):")
print(df["VAL_TOT"].describe())
print(f"Skewness (VAL_TOT): {df['VAL_TOT'].skew():.2f}")
print(f"Kurtosis (VAL_TOT): {df['VAL_TOT'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df["VAL_TOT"], kde=True, bins=50, color="lightgreen")
plt.title("Distribution of Total Hospitalization Cost")
plt.xlabel("Total Cost")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
sns.boxplot(y="VAL_TOT", data=df, color="orange")
plt.title("Box Plot of Total Hospitalization Cost")
plt.ylabel("Total Cost")
plt.show()

# DIAS_PERM (Original Days of Stay)
print("\nAnalysis of the 'DIAS_PERM' Variable (Original Days of Stay):")
print(df["DIAS_PERM"].describe())
print(f"Skewness (DIAS_PERM): {df['DIAS_PERM'].skew():.2f}")
print(f"Kurtosis (DIAS_PERM): {df['DIAS_PERM'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df["DIAS_PERM"], kde=True, bins=30, color="purple")
plt.title("Distribution of Original Days of Stay")
plt.xlabel("Days of Stay")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
sns.boxplot(y="DIAS_PERM", data=df, color="pink")
plt.title("Box Plot of Original Days of Stay")
plt.ylabel("Days of Stay")
plt.show()

# DIAS_INTERNACAO (Calculated Hospitalization Days)
print("\nAnalysis of the 'DIAS_INTERNACAO' Variable (Calculated Hospitalization Days):")
print(df["DIAS_INTERNACAO"].describe())
print(f"Skewness (DIAS_INTERNACAO): {df['DIAS_INTERNACAO'].skew():.2f}")
print(f"Kurtosis (DIAS_INTERNACAO): {df['DIAS_INTERNACAO'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df["DIAS_INTERNACAO"], kde=True, bins=30, color="teal")
plt.title("Distribution of Calculated Hospitalization Days")
plt.xlabel("Hospitalization Days")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
sns.boxplot(y="DIAS_INTERNACAO", data=df, color="gold")
plt.title("Box Plot of Calculated Hospitalization Days")
plt.ylabel("Hospitalization Days")
plt.show()

# 3. Correlation between Numerical Variables
print("\n--- Correlation between Numerical Variables ---")
numerical_cols = [
    "IDADE",
    "VAL_TOT",
    "DIAS_PERM",
    "DIAS_INTERNACAO",
    "munResLat",
    "munResLon",
    "munResAlt",
    "munResArea",
]
correlation_matrix = df[numerical_cols].corr()
print("Correlation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix between Numerical Variables")
plt.show()

# 4. Analysis of Relationships between Variables (Examples)

# VAL_TOT by SEXO
print("\nAnalysis of VAL_TOT by SEXO:")
plt.figure(figsize=(8, 6))
sns.boxplot(x="SEXO", y="VAL_TOT", data=df, palette="viridis")
plt.title("Total Hospitalization Cost by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Hospitalization Cost")
plt.ylim(
    0, df["VAL_TOT"].quantile(0.99)
)  # Limiting y-axis to focus on the majority of data
plt.show()

# DIAS_PERM by SEXO
print("\nAnalysis of DIAS_PERM by SEXO:")
plt.figure(figsize=(8, 6))
sns.boxplot(x="SEXO", y="DIAS_PERM", data=df, palette="plasma")
plt.title("Days of Stay by Gender")
plt.xlabel("Gender")
plt.ylabel("Days of Stay")
plt.ylim(
    0, df["DIAS_PERM"].quantile(0.99)
)  # Limiting y-axis to focus on the majority of data
plt.show()

# VAL_TOT by faixa_etaria_corrigida
print("\nAnalysis of VAL_TOT by Age Group:")

