import pandas as pd

# Read the CSV file
df = pd.read_csv("../dados/FraturasCorrigido.csv")

# Display basic information about the DataFrame
print("Informações iniciais do DataFrame:")
df.info()

# Display the first 5 rows of the DataFrame
print("\nPrimeiras 5 linhas do DataFrame:")
print(df.head())

# Check for missing values
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

# Display descriptive statistics for numerical columns
print("\nEstatísticas descritivas para colunas numéricas:")
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

print("\n--- Análise Estatística Detalhada ---")

# 1. Análise de Variáveis Categóricas

# SEXO
print("\nAnálise da Variável 'SEXO':")
sexo_counts = df["SEXO"].value_counts()
sexo_proportions = df["SEXO"].value_counts(normalize=True) * 100
print(pd.DataFrame({"Contagem": sexo_counts, "Proporção (%)": sexo_proportions}))

plt.figure(figsize=(8, 6))
sns.countplot(x="SEXO", data=df, palette="viridis")
plt.title("Distribuição de Gênero")
plt.xlabel("Gênero")
plt.ylabel("Contagem")
plt.show()

# MORTE
print("\nAnálise da Variável 'MORTE':")
morte_counts = df["MORTE"].value_counts()
morte_proportions = df["MORTE"].value_counts(normalize=True) * 100
print(pd.DataFrame({"Contagem": morte_counts, "Proporção (%)": morte_proportions}))

plt.figure(figsize=(8, 6))
sns.countplot(x="MORTE", data=df, palette="plasma")
plt.title("Distribuição de Óbitos")
plt.xlabel("Óbito")
plt.ylabel("Contagem")
plt.show()

# faixa_etaria_corrigida
print("\nAnálise da Variável 'faixa_etaria_corrigida':")
faixa_etaria_counts = df["faixa_etaria_corrigida"].value_counts().sort_index()
faixa_etaria_proportions = (
    df["faixa_etaria_corrigida"].value_counts(normalize=True).sort_index() * 100
)
print(
    pd.DataFrame(
        {"Contagem": faixa_etaria_counts, "Proporção (%)": faixa_etaria_proportions}
    )
)

plt.figure(figsize=(12, 7))
sns.countplot(
    y="faixa_etaria_corrigida",
    data=df,
    order=faixa_etaria_counts.index,
    palette="cividis",
)
plt.title("Distribuição por Faixa Etária Corrigida")
plt.xlabel("Contagem")
plt.ylabel("Faixa Etária")
plt.show()

# tipo_fratura
print("\nAnálise da Variável 'tipo_fratura':")
tipo_fratura_counts = df["tipo_fratura"].value_counts()
tipo_fratura_proportions = df["tipo_fratura"].value_counts(normalize=True) * 100
print(
    pd.DataFrame(
        {"Contagem": tipo_fratura_counts, "Proporção (%)": tipo_fratura_proportions}
    )
)

plt.figure(figsize=(12, 8))
sns.countplot(
    y="tipo_fratura", data=df, order=tipo_fratura_counts.index, palette="magma"
)
plt.title("Distribuição por Tipo de Fratura")
plt.xlabel("Contagem")
plt.ylabel("Tipo de Fratura")
plt.show()

# regiao
print("\nAnálise da Variável 'regiao':")
regiao_counts = df["regiao"].value_counts()
regiao_proportions = df["regiao"].value_counts(normalize=True) * 100
print(pd.DataFrame({"Contagem": regiao_counts, "Proporção (%)": regiao_proportions}))

plt.figure(figsize=(10, 7))
sns.countplot(y="regiao", data=df, order=regiao_counts.index, palette="GnBu_d")
plt.title("Distribuição por Região da Fratura")
plt.xlabel("Contagem")
plt.ylabel("Região")
plt.show()

# tem_osteoporose
print("\nAnálise da Variável 'tem_osteoporose':")
osteoporose_counts = df["tem_osteoporose"].value_counts()
osteoporose_proportions = df["tem_osteoporose"].value_counts(normalize=True) * 100
print(
    pd.DataFrame(
        {"Contagem": osteoporose_counts, "Proporção (%)": osteoporose_proportions}
    )
)

# obito_hospitalar (rechecking as it was 0 for all)
print("\nAnálise da Variável 'obito_hospitalar':")
obito_hospitalar_counts = df["obito_hospitalar"].value_counts()
obito_hospitalar_proportions = df["obito_hospitalar"].value_counts(normalize=True) * 100
print(
    pd.DataFrame(
        {
            "Contagem": obito_hospitalar_counts,
            "Proporção (%)": obito_hospitalar_proportions,
        }
    )
)

# ano_internacao
print("\nAnálise da Variável 'ano_internacao':")
ano_internacao_counts = df["ano_internacao"].value_counts().sort_index()
ano_internacao_proportions = (
    df["ano_internacao"].value_counts(normalize=True).sort_index() * 100
)
print(
    pd.DataFrame(
        {"Contagem": ano_internacao_counts, "Proporção (%)": ano_internacao_proportions}
    )
)

plt.figure(figsize=(10, 6))
sns.countplot(x="ano_internacao", data=df, palette="coolwarm")
plt.title("Número de Internações por Ano")
plt.xlabel("Ano de Internação")
plt.ylabel("Contagem")
plt.show()

# 2. Análise de Variáveis Numéricas

# IDADE
print("\nAnálise da Variável 'IDADE':")
print(df["IDADE"].describe())
print(f"Skewness (IDADE): {df['IDADE'].skew():.2f}")
print(f"Kurtosis (IDADE): {df['IDADE'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df["IDADE"], kde=True, bins=30, color="skyblue")
plt.title("Distribuição de Idade")
plt.xlabel("Idade")
plt.ylabel("Frequência")

plt.subplot(1, 2, 2)
sns.boxplot(y="IDADE", data=df, color="lightcoral")
plt.title("Box Plot da Idade")
plt.ylabel("Idade")
plt.show()

# VAL_TOT
print("\nAnálise da Variável 'VAL_TOT' (Valor Total da Internação):")
print(df["VAL_TOT"].describe())
print(f"Skewness (VAL_TOT): {df['VAL_TOT'].skew():.2f}")
print(f"Kurtosis (VAL_TOT): {df['VAL_TOT'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df["VAL_TOT"], kde=True, bins=50, color="lightgreen")
plt.title("Distribuição do Valor Total da Internação")
plt.xlabel("Valor Total")
plt.ylabel("Frequência")

plt.subplot(1, 2, 2)
sns.boxplot(y="VAL_TOT", data=df, color="orange")
plt.title("Box Plot do Valor Total da Internação")
plt.ylabel("Valor Total")
plt.show()

# DIAS_PERM
print("\nAnálise da Variável 'DIAS_PERM' (Dias de Permanência Originais):")
print(df["DIAS_PERM"].describe())
print(f"Skewness (DIAS_PERM): {df['DIAS_PERM'].skew():.2f}")
print(f"Kurtosis (DIAS_PERM): {df['DIAS_PERM'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df["DIAS_PERM"], kde=True, bins=30, color="purple")
plt.title("Distribuição dos Dias de Permanência Originais")
plt.xlabel("Dias de Permanência")
plt.ylabel("Frequência")

plt.subplot(1, 2, 2)
sns.boxplot(y="DIAS_PERM", data=df, color="pink")
plt.title("Box Plot dos Dias de Permanência Originais")
plt.ylabel("Dias de Permanência")
plt.show()

# DIAS_INTERNACAO (Recém-calculada)
print("\nAnálise da Variável 'DIAS_INTERNACAO' (Dias de Internação Calculados):")
print(df["DIAS_INTERNACAO"].describe())
print(f"Skewness (DIAS_INTERNACAO): {df['DIAS_INTERNACAO'].skew():.2f}")
print(f"Kurtosis (DIAS_INTERNACAO): {df['DIAS_INTERNACAO'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df["DIAS_INTERNACAO"], kde=True, bins=30, color="teal")
plt.title("Distribuição dos Dias de Internação Calculados")
plt.xlabel("Dias de Internação")
plt.ylabel("Frequência")

plt.subplot(1, 2, 2)
sns.boxplot(y="DIAS_INTERNACAO", data=df, color="gold")
plt.title("Box Plot dos Dias de Internação Calculados")
plt.ylabel("Dias de Internação")
plt.show()

# 3. Correlação entre Variáveis Numéricas
print("\n--- Correlação entre Variáveis Numéricas ---")
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
print("Matriz de Correlação:")
print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlação entre Variáveis Numéricas")
plt.show()

# 4. Análise de Relação entre Variáveis (Exemplos)

# VAL_TOT por SEXO
print("\nAnálise de VAL_TOT por SEXO:")
plt.figure(figsize=(8, 6))
sns.boxplot(x="SEXO", y="VAL_TOT", data=df, palette="viridis")
plt.title("Valor Total da Internação por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Valor Total da Internação")
plt.ylim(
    0, df["VAL_TOT"].quantile(0.99)
)  # Limiting y-axis to focus on the majority of data
plt.show()

# DIAS_PERM por SEXO
print("\nAnálise de DIAS_PERM por SEXO:")
plt.figure(figsize=(8, 6))
sns.boxplot(x="SEXO", y="DIAS_PERM", data=df, palette="plasma")
plt.title("Dias de Permanência por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Dias de Permanência")
plt.ylim(
    0, df["DIAS_PERM"].quantile(0.99)
)  # Limiting y-axis to focus on the majority of data
plt.show()

# VAL_TOT por faixa_etaria_corrigida
print("\nAnálise de VAL_TOT por Faixa Etária:")

# NOTA: O script original foi truncado durante a leitura.
# Pode haver mais código de análise após este ponto.
# Por favor, verifique o arquivo original e complete se necessário.
