# Código inicial de analise

```basic
import pandas as pd

# Read the CSV file
df = pd.read_csv('FraturasCorrigido.csv')

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
```

```basic
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Drop completely null columns
df = df.drop(columns=['DIAGSEC8', 'DIAGSEC9'])

# Convert date columns to datetime objects
df['DT_INTER'] = pd.to_datetime(df['DT_INTER'])
df['DT_SAIDA'] = pd.to_datetime(df['DT_SAIDA'])

# Calculate days of hospitalization
df['DIAS_INTERNACAO'] = (df['DT_SAIDA'] - df['DT_INTER']).dt.days

# --- In-depth Descriptive Statistics and Visualization ---

print("\n--- Análise Estatística Detalhada ---")

# 1. Análise de Variáveis Categóricas

# SEXO
print("\nAnálise da Variável 'SEXO':")
sexo_counts = df['SEXO'].value_counts()
sexo_proportions = df['SEXO'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Contagem': sexo_counts, 'Proporção (%)': sexo_proportions}))

plt.figure(figsize=(8, 6))
sns.countplot(x='SEXO', data=df, palette='viridis')
plt.title('Distribuição de Gênero')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.show()

# MORTE
print("\nAnálise da Variável 'MORTE':")
morte_counts = df['MORTE'].value_counts()
morte_proportions = df['MORTE'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Contagem': morte_counts, 'Proporção (%)': morte_proportions}))

plt.figure(figsize=(8, 6))
sns.countplot(x='MORTE', data=df, palette='plasma')
plt.title('Distribuição de Óbitos')
plt.xlabel('Óbito')
plt.ylabel('Contagem')
plt.show()

# faixa_etaria_corrigida
print("\nAnálise da Variável 'faixa_etaria_corrigida':")
faixa_etaria_counts = df['faixa_etaria_corrigida'].value_counts().sort_index()
faixa_etaria_proportions = df['faixa_etaria_corrigida'].value_counts(normalize=True).sort_index() * 100
print(pd.DataFrame({'Contagem': faixa_etaria_counts, 'Proporção (%)': faixa_etaria_proportions}))

plt.figure(figsize=(12, 7))
sns.countplot(y='faixa_etaria_corrigida', data=df, order=faixa_etaria_counts.index, palette='cividis')
plt.title('Distribuição por Faixa Etária Corrigida')
plt.xlabel('Contagem')
plt.ylabel('Faixa Etária')
plt.show()

# tipo_fratura
print("\nAnálise da Variável 'tipo_fratura':")
tipo_fratura_counts = df['tipo_fratura'].value_counts()
tipo_fratura_proportions = df['tipo_fratura'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Contagem': tipo_fratura_counts, 'Proporção (%)': tipo_fratura_proportions}))

plt.figure(figsize=(12, 8))
sns.countplot(y='tipo_fratura', data=df, order=tipo_fratura_counts.index, palette='magma')
plt.title('Distribuição por Tipo de Fratura')
plt.xlabel('Contagem')
plt.ylabel('Tipo de Fratura')
plt.show()

# regiao
print("\nAnálise da Variável 'regiao':")
regiao_counts = df['regiao'].value_counts()
regiao_proportions = df['regiao'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Contagem': regiao_counts, 'Proporção (%)': regiao_proportions}))

plt.figure(figsize=(10, 7))
sns.countplot(y='regiao', data=df, order=regiao_counts.index, palette='GnBu_d')
plt.title('Distribuição por Região da Fratura')
plt.xlabel('Contagem')
plt.ylabel('Região')
plt.show()

# tem_osteoporose
print("\nAnálise da Variável 'tem_osteoporose':")
osteoporose_counts = df['tem_osteoporose'].value_counts()
osteoporose_proportions = df['tem_osteoporose'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Contagem': osteoporose_counts, 'Proporção (%)': osteoporose_proportions}))

# obito_hospitalar (rechecking as it was 0 for all)
print("\nAnálise da Variável 'obito_hospitalar':")
obito_hospitalar_counts = df['obito_hospitalar'].value_counts()
obito_hospitalar_proportions = df['obito_hospitalar'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Contagem': obito_hospitalar_counts, 'Proporção (%)': obito_hospitalar_proportions}))

# ano_internacao
print("\nAnálise da Variável 'ano_internacao':")
ano_internacao_counts = df['ano_internacao'].value_counts().sort_index()
ano_internacao_proportions = df['ano_internacao'].value_counts(normalize=True).sort_index() * 100
print(pd.DataFrame({'Contagem': ano_internacao_counts, 'Proporção (%)': ano_internacao_proportions}))

plt.figure(figsize=(10, 6))
sns.countplot(x='ano_internacao', data=df, palette='coolwarm')
plt.title('Número de Internações por Ano')
plt.xlabel('Ano de Internação')
plt.ylabel('Contagem')
plt.show()

# 2. Análise de Variáveis Numéricas

# IDADE
print("\nAnálise da Variável 'IDADE':")
print(df['IDADE'].describe())
print(f"Skewness (IDADE): {df['IDADE'].skew():.2f}")
print(f"Kurtosis (IDADE): {df['IDADE'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['IDADE'], kde=True, bins=30, color='skyblue')
plt.title('Distribuição de Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
sns.boxplot(y='IDADE', data=df, color='lightcoral')
plt.title('Box Plot da Idade')
plt.ylabel('Idade')
plt.show()

# VAL_TOT
print("\nAnálise da Variável 'VAL_TOT' (Valor Total da Internação):")
print(df['VAL_TOT'].describe())
print(f"Skewness (VAL_TOT): {df['VAL_TOT'].skew():.2f}")
print(f"Kurtosis (VAL_TOT): {df['VAL_TOT'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['VAL_TOT'], kde=True, bins=50, color='lightgreen')
plt.title('Distribuição do Valor Total da Internação')
plt.xlabel('Valor Total')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
sns.boxplot(y='VAL_TOT', data=df, color='orange')
plt.title('Box Plot do Valor Total da Internação')
plt.ylabel('Valor Total')
plt.show()

# DIAS_PERM
print("\nAnálise da Variável 'DIAS_PERM' (Dias de Permanência Originais):")
print(df['DIAS_PERM'].describe())
print(f"Skewness (DIAS_PERM): {df['DIAS_PERM'].skew():.2f}")
print(f"Kurtosis (DIAS_PERM): {df['DIAS_PERM'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['DIAS_PERM'], kde=True, bins=30, color='purple')
plt.title('Distribuição dos Dias de Permanência Originais')
plt.xlabel('Dias de Permanência')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
sns.boxplot(y='DIAS_PERM', data=df, color='pink')
plt.title('Box Plot dos Dias de Permanência Originais')
plt.ylabel('Dias de Permanência')
plt.show()

# DIAS_INTERNACAO (Recém-calculada)
print("\nAnálise da Variável 'DIAS_INTERNACAO' (Dias de Internação Calculados):")
print(df['DIAS_INTERNACAO'].describe())
print(f"Skewness (DIAS_INTERNACAO): {df['DIAS_INTERNACAO'].skew():.2f}")
print(f"Kurtosis (DIAS_INTERNACAO): {df['DIAS_INTERNACAO'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['DIAS_INTERNACAO'], kde=True, bins=30, color='teal')
plt.title('Distribuição dos Dias de Internação Calculados')
plt.xlabel('Dias de Internação')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
sns.boxplot(y='DIAS_INTERNACAO', data=df, color='gold')
plt.title('Box Plot dos Dias de Internação Calculados')
plt.ylabel('Dias de Internação')
plt.show()

# 3. Correlação entre Variáveis Numéricas
print("\n--- Correlação entre Variáveis Numéricas ---")
numerical_cols = ['IDADE', 'VAL_TOT', 'DIAS_PERM', 'DIAS_INTERNACAO', 'munResLat', 'munResLon', 'munResAlt', 'munResArea']
correlation_matrix = df[numerical_cols].corr()
print("Matriz de Correlação:")
print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlação entre Variáveis Numéricas')
plt.show()

# 4. Análise de Relação entre Variáveis (Exemplos)

# VAL_TOT por SEXO
print("\nAnálise de VAL_TOT por SEXO:")
plt.figure(figsize=(8, 6))
sns.boxplot(x='SEXO', y='VAL_TOT', data=df, palette='viridis')
plt.title('Valor Total da Internação por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Valor Total da Internação')
plt.ylim(0, df['VAL_TOT'].quantile(0.99)) # Limiting y-axis to focus on the majority of data
plt.show()

# DIAS_PERM por SEXO
print("\nAnálise de DIAS_PERM por SEXO:")
plt.figure(figsize=(8, 6))
sns.boxplot(x='SEXO', y='DIAS_PERM', data=df, palette='plasma')
plt.title('Dias de Permanência por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Dias de Permanência')
plt.ylim(0, df['DIAS_PERM'].quantile(0.99)) # Limiting y-axis to focus on the majority of data
plt.show()

# VAL_TOT por faixa_etaria_corrigida
print("\nAnálise de VAL_TOT por Faixa Etária:")
plt.figure(figsize=(14, 8))
sns.boxplot(x='faixa_etaria_corrigida', y='VAL_TOT', data=df, order=faixa_etaria_counts.index, palette='cividis')
plt.title('Valor Total da Internação por Faixa Etária')
plt.xlabel('Faixa Etária')
plt.ylabel('Valor Total da Internação')
plt.ylim(0, df['VAL_TOT'].quantile(0.99))
plt.xticks(rotation=45)
plt.show()

# DIAS_PERM por faixa_etaria_corrigida
print("\nAnálise de DIAS_PERM por Faixa Etária:")
plt.figure(figsize=(14, 8))
sns.boxplot(x='faixa_etaria_corrigida', y='DIAS_PERM', data=df, order=faixa_etaria_counts.index, palette='magma')
plt.title('Dias de Permanência por Faixa Etária')
plt.xlabel('Faixa Etária')
plt.ylabel('Dias de Permanência')
plt.ylim(0, df['DIAS_PERM'].quantile(0.99))
plt.xticks(rotation=45)
plt.show()

# VAL_TOT por tipo_fratura
print("\nAnálise de VAL_TOT por Tipo de Fratura:")
plt.figure(figsize=(14, 8))
sns.boxplot(y='tipo_fratura', x='VAL_TOT', data=df, order=tipo_fratura_counts.index, palette='GnBu_d')
plt.title('Valor Total da Internação por Tipo de Fratura')
plt.xlabel('Valor Total da Internação')
plt.ylabel('Tipo de Fratura')
plt.xlim(0, df['VAL_TOT'].quantile(0.99))
plt.show()

# DIAS_PERM por tipo_fratura
print("\nAnálise de DIAS_PERM por Tipo de Fratura:")
plt.figure(figsize=(14, 8))
sns.boxplot(y='tipo_fratura', x='DIAS_PERM', data=df, order=tipo_fratura_counts.index, palette='coolwarm')
plt.title('Dias de Permanência por Tipo de Fratura')
plt.xlabel('Dias de Permanência')
plt.ylabel('Tipo de Fratura')
plt.xlim(0, df['DIAS_PERM'].quantile(0.99))
plt.show()

# Análise de Óbito Hospitalar (considerando que era 0 para todos, vamos reconfirmar)
if df['obito_hospitalar'].sum() == 0:
    print("\nAVISO: A coluna 'obito_hospitalar' contém apenas valores 0, indicando que não há óbitos hospitalares registrados neste dataset. Isso pode ser um problema de coleta de dados ou o dataset não captura esse evento.")
else:
    print("\nAnálise de Óbito Hospitalar por Faixa Etária:")
    obito_faixa_etaria = df.groupby('faixa_etaria_corrigida')['obito_hospitalar'].value_counts(normalize=True).unstack() * 100
    print(obito_faixa_etaria)

    plt.figure(figsize=(12, 7))
    obito_faixa_etaria.plot(kind='bar', stacked=True, colormap='Accent')
    plt.title('Proporção de Óbito Hospitalar por Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Proporção (%)')
    plt.xticks(rotation=45)
    plt.legend(title='Óbito Hospitalar', labels=['Não', 'Sim'])
    plt.show()
```

```basic
--- Análise Estatística Detalhada ---

Análise da Variável 'SEXO':
           Contagem  Proporção (%)
Feminino     227783      64.661665
Masculino    124486      35.338335

Análise da Variável 'MORTE':
     Contagem  Proporção (%)
Não    342905      97.341804
Sim      9364       2.658196

Análise da Variável 'faixa_etaria_corrigida':
                   Contagem  Proporção (%)
60-69 anos           106062      30.108241
70-79 anos            98669      28.009561
80-89 anos            81949      23.263188
90+ anos              22981       6.523708
Abaixo de 60 anos     42608      12.095302

Análise da Variável 'tipo_fratura':
                 Contagem  Proporção (%)
Fêmur proximal     175183      49.729894
Antebraço/Punho    119599      33.951043
Úmero               46348      13.156991
Vértebra             7673       2.178165
Quadril/Pelve        3466       0.983907

Análise da Variável 'regiao':
                  Contagem  Proporção (%)
Não classificado    352269          100.0

Análise da Variável 'tem_osteoporose':
   Contagem  Proporção (%)
0    352179      99.974451
1        90       0.025549

Análise da Variável 'obito_hospitalar':
   Contagem  Proporção (%)
0    352269          100.0

Análise da Variável 'ano_internacao':
      Contagem  Proporção (%)
2019     77373      21.964181
2020     80127      22.745970
2021     89004      25.265919
2023    105765      30.023931

Análise da Variável 'IDADE':
count    352269.000000
mean         66.822000
std          23.601369
min           7.000000
25%          64.000000
50%          72.000000
75%          81.000000
max          99.000000
Name: IDADE, dtype: float64
Skewness (IDADE): -1.68
Kurtosis (IDADE): 1.87

Análise da Variável 'VAL_TOT' (Valor Total da Internação):
count    352269.000000
mean       1837.100464
std        2157.995485
min          21.980000
25%         327.940000
50%        1064.690000
75%        2534.670000
max       55462.790000
Name: VAL_TOT, dtype: float64
Skewness (VAL_TOT): 3.60
Kurtosis (VAL_TOT): 31.79

Análise da Variável 'DIAS_PERM' (Dias de Permanência Originais):
count    352269.000000
mean          5.682663
std           6.608256
min           0.000000
25%           2.000000
50%           4.000000
75%           7.000000
max         305.000000
Name: DIAS_PERM, dtype: float64
Skewness (DIAS_PERM): 4.17
Kurtosis (DIAS_PERM): 52.09

Análise da Variável 'DIAS_INTERNACAO' (Dias de Internação Calculados):
count    352269.000000
mean          5.689800
std           6.704931
min           0.000000
25%           2.000000
50%           4.000000
75%           7.000000
max         317.000000
Name: DIAS_INTERNACAO, dtype: float64
Skewness (DIAS_INTERNACAO): 4.84
Kurtosis (DIAS_INTERNACAO): 78.91

--- Correlação entre Variáveis Numéricas ---
Matriz de Correlação:
                    IDADE   VAL_TOT  DIAS_PERM  DIAS_INTERNACAO  munResLat  munResLon  munResAlt  munResArea
IDADE            1.000000  0.297587   0.249131         0.245680  -0.149755   0.020971   0.060588   -0.068444
VAL_TOT          0.297587  1.000000   0.475463         0.468795  -0.082131   0.010429   0.022640   -0.037425
DIAS_PERM        0.249131  0.475463   1.000000         0.988911  -0.010547   0.076020  -0.082090    0.000782
DIAS_INTERNACAO  0.245680  0.468795   0.988911         1.000000  -0.010907   0.074873  -0.079594    0.000562
munResLat       -0.149755 -0.082131  -0.010547        -0.010907   1.000000   0.467383  -0.338821    0.160748
munResLon        0.020971  0.010429   0.076020         0.074873   0.467383   1.000000  -0.228519   -0.235924
munResAlt        0.060588  0.022640  -0.082090        -0.079594  -0.338821  -0.228519   1.000000   -0.065446
munResArea      -0.068444 -0.037425   0.000782         0.000562   0.160748  -0.235924  -0.065446    1.000000

Análise de VAL_TOT por SEXO:

Análise de DIAS_PERM por SEXO:

Análise de VAL_TOT por Faixa Etária:

Análise de DIAS_PERM por Faixa Etária:

Análise de VAL_TOT por Tipo de Fratura:

Análise de DIAS_PERM por Tipo de Fratura:

AVISO: A coluna 'obito_hospitalar' contém apenas valores 0, indicando que não há óbitos hospitalares registrados neste dataset. Isso pode ser um problema de coleta de dados ou o dataset não captura esse evento.

```