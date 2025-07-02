import pandas as pd

# Read the CSV file
df = pd.read_csv('FraturasCorrigido.csv')

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
df = df.drop(columns=['DIAGSEC8', 'DIAGSEC9'])

# Convert date columns to datetime objects
df['DT_INTER'] = pd.to_datetime(df['DT_INTER'])
df['DT_SAIDA'] = pd.to_datetime(df['DT_SAIDA'])

# Calculate days of hospitalization
df['DIAS_INTERNACAO'] = (df['DT_SAIDA'] - df['DT_INTER']).dt.days

# --- In-depth Descriptive Statistics and Visualization ---

print("\n--- Detailed Statistical Analysis ---")

# 1. Analysis of Categorical Variables

# SEXO (Gender)
print("\nAnalysis of the 'SEXO' Variable:")
sexo_counts = df['SEXO'].value_counts()
sexo_proportions = df['SEXO'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Count': sexo_counts, 'Proportion (%)': sexo_proportions}))

plt.figure(figsize=(8, 6))
sns.countplot(x='SEXO', data=df, palette='viridis')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# MORTE (Death)
print("\nAnalysis of the 'MORTE' Variable:")
morte_counts = df['MORTE'].value_counts()
morte_proportions = df['MORTE'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Count': morte_counts, 'Proportion (%)': morte_proportions}))

plt.figure(figsize=(8, 6))
sns.countplot(x='MORTE', data=df, palette='plasma')
plt.title('Distribution of Deaths')
plt.xlabel('Death')
plt.ylabel('Count')
plt.show()

# faixa_etaria_corrigida (Corrected Age Group)
print("\nAnalysis of the 'faixa_etaria_corrigida' Variable:")
faixa_etaria_counts = df['faixa_etaria_corrigida'].value_counts().sort_index()
faixa_etaria_proportions = df['faixa_etaria_corrigida'].value_counts(normalize=True).sort_index() * 100
print(pd.DataFrame({'Count': faixa_etaria_counts, 'Proportion (%)': faixa_etaria_proportions}))

plt.figure(figsize=(12, 7))
sns.countplot(y='faixa_etaria_corrigida', data=df, order=faixa_etaria_counts.index, palette='cividis')
plt.title('Distribution by Corrected Age Group')
plt.xlabel('Count')
plt.ylabel('Age Group')
plt.show()

# tipo_fratura (Fracture Type)
print("\nAnalysis of the 'tipo_fratura' Variable:")
tipo_fratura_counts = df['tipo_fratura'].value_counts()
tipo_fratura_proportions = df['tipo_fratura'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Count': tipo_fratura_counts, 'Proportion (%)': tipo_fratura_proportions}))

plt.figure(figsize=(12, 8))
sns.countplot(y='tipo_fratura', data=df, order=tipo_fratura_counts.index, palette='magma')
plt.title('Distribution by Fracture Type')
plt.xlabel('Count')
plt.ylabel('Fracture Type')
plt.show()

# regiao (Region)
print("\nAnalysis of the 'regiao' Variable:")
regiao_counts = df['regiao'].value_counts()
regiao_proportions = df['regiao'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Count': regiao_counts, 'Proportion (%)': regiao_proportions}))

plt.figure(figsize=(10, 7))
sns.countplot(y='regiao', data=df, order=regiao_counts.index, palette='GnBu_d')
plt.title('Distribution by Fracture Region')
plt.xlabel('Count')
plt.ylabel('Region')
plt.show()

# tem_osteoporose (Has Osteoporosis)
print("\nAnalysis of the 'tem_osteoporose' Variable:")
osteoporose_counts = df['tem_osteoporose'].value_counts()
osteoporose_proportions = df['tem_osteoporose'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Count': osteoporose_counts, 'Proportion (%)': osteoporose_proportions}))

# obito_hospitalar (Hospital Death) (rechecking as it was 0 for all)
print("\nAnalysis of the 'obito_hospitalar' Variable:")
obito_hospitalar_counts = df['obito_hospitalar'].value_counts()
obito_hospitalar_proportions = df['obito_hospitalar'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Count': obito_hospitalar_counts, 'Proportion (%)': obito_hospitalar_proportions}))

# ano_internacao (Year of Hospitalization)
print("\nAnalysis of the 'ano_internacao' Variable:")
ano_internacao_counts = df['ano_internacao'].value_counts().sort_index()
ano_internacao_proportions = df['ano_internacao'].value_counts(normalize=True).sort_index() * 100
print(pd.DataFrame({'Count': ano_internacao_counts, 'Proportion (%)': ano_internacao_proportions}))

plt.figure(figsize=(10, 6))
sns.countplot(x='ano_internacao', data=df, palette='coolwarm')
plt.title('Number of Hospitalizations per Year')
plt.xlabel('Year of Hospitalization')
plt.ylabel('Count')
plt.show()

# 2. Analysis of Numerical Variables

# IDADE (Age)
print("\nAnalysis of the 'IDADE' Variable:")
print(df['IDADE'].describe())
print(f"Skewness (IDADE): {df['IDADE'].skew():.2f}")
print(f"Kurtosis (IDADE): {df['IDADE'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['IDADE'], kde=True, bins=30, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
sns.boxplot(y='IDADE', data=df, color='lightcoral')
plt.title('Age Box Plot')
plt.ylabel('Age')
plt.show()

# VAL_TOT (Total Hospitalization Cost)
print("\nAnalysis of the 'VAL_TOT' Variable (Total Hospitalization Cost):")
print(df['VAL_TOT'].describe())
print(f"Skewness (VAL_TOT): {df['VAL_TOT'].skew():.2f}")
print(f"Kurtosis (VAL_TOT): {df['VAL_TOT'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['VAL_TOT'], kde=True, bins=50, color='lightgreen')
plt.title('Distribution of Total Hospitalization Cost')
plt.xlabel('Total Cost')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
sns.boxplot(y='VAL_TOT', data=df, color='orange')
plt.title('Box Plot of Total Hospitalization Cost')
plt.ylabel('Total Cost')
plt.show()

# DIAS_PERM (Original Days of Stay)
print("\nAnalysis of the 'DIAS_PERM' Variable (Original Days of Stay):")
print(df['DIAS_PERM'].describe())
print(f"Skewness (DIAS_PERM): {df['DIAS_PERM'].skew():.2f}")
print(f"Kurtosis (DIAS_PERM): {df['DIAS_PERM'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['DIAS_PERM'], kde=True, bins=30, color='purple')
plt.title('Distribution of Original Days of Stay')
plt.xlabel('Days of Stay')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
sns.boxplot(y='DIAS_PERM', data=df, color='pink')
plt.title('Box Plot of Original Days of Stay')
plt.ylabel('Days of Stay')
plt.show()

# DIAS_INTERNACAO (Calculated Hospitalization Days)
print("\nAnalysis of the 'DIAS_INTERNACAO' Variable (Calculated Hospitalization Days):")
print(df['DIAS_INTERNACAO'].describe())
print(f"Skewness (DIAS_INTERNACAO): {df['DIAS_INTERNACAO'].skew():.2f}")
print(f"Kurtosis (DIAS_INTERNACAO): {df['DIAS_INTERNACAO'].kurtosis():.2f}")

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['DIAS_INTERNACAO'], kde=True, bins=30, color='teal')
plt.title('Distribution of Calculated Hospitalization Days')
plt.xlabel('Hospitalization Days')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
sns.boxplot(y='DIAS_INTERNACAO', data=df, color='gold')
plt.title('Box Plot of Calculated Hospitalization Days')
plt.ylabel('Hospitalization Days')
plt.show()

# 3. Correlation between Numerical Variables
print("\n--- Correlation between Numerical Variables ---")
numerical_cols = ['IDADE', 'VAL_TOT', 'DIAS_PERM', 'DIAS_INTERNACAO', 'munResLat', 'munResLon', 'munResAlt', 'munResArea']
correlation_matrix = df[numerical_cols].corr()
print("Correlation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix between Numerical Variables')
plt.show()

# 4. Analysis of Relationships between Variables (Examples)

# VAL_TOT by SEXO
print("\nAnalysis of VAL_TOT by SEXO:")
plt.figure(figsize=(8, 6))
sns.boxplot(x='SEXO', y='VAL_TOT', data=df, palette='viridis')
plt.title('Total Hospitalization Cost by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Hospitalization Cost')
plt.ylim(0, df['VAL_TOT'].quantile(0.99)) # Limiting y-axis to focus on the majority of data
plt.show()

# DIAS_PERM by SEXO
print("\nAnalysis of DIAS_PERM by SEXO:")
plt.figure(figsize=(8, 6))
sns.boxplot(x='SEXO', y='DIAS_PERM', data=df, palette='plasma')
plt.title('Days of Stay by Gender')
plt.xlabel('Gender')
plt.ylabel('Days of Stay')
plt.ylim(0, df['DIAS_PERM'].quantile(0.99)) # Limiting y-axis to focus on the majority of data
plt.show()

# VAL_TOT by faixa_etaria_corrigida
print("\nAnalysis of VAL_TOT by Age Group:")
plt.figure(figsize=(14, 8))
sns.boxplot(x='faixa_etaria_corrigida', y='VAL_TOT', data=df, order=faixa_etaria_counts.index, palette='cividis')
plt.title('Total Hospitalization Cost by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Total Hospitalization Cost')
plt.ylim(0, df['VAL_TOT'].quantile(0.99))
plt.xticks(rotation=45)
plt.show()

# DIAS_PERM by faixa_etaria_corrigida
print("\nAnalysis of DIAS_PERM by Age Group:")
plt.figure(figsize=(14, 8))
sns.boxplot(x='faixa_etaria_corrigida', y='DIAS_PERM', data=df, order=faixa_etaria_counts.index, palette='magma')
plt.title('Days of Stay by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Days of Stay')
plt.ylim(0, df['DIAS_PERM'].quantile(0.99))
plt.xticks(rotation=45)
plt.show()

# VAL_TOT by tipo_fratura
print("\nAnalysis of VAL_TOT by Fracture Type:")
plt.figure(figsize=(14, 8))
sns.boxplot(y='tipo_fratura', x='VAL_TOT', data=df, order=tipo_fratura_counts.index, palette='GnBu_d')
plt.title('Total Hospitalization Cost by Fracture Type')
plt.xlabel('Total Hospitalization Cost')
plt.ylabel('Fracture Type')
plt.xlim(0, df['VAL_TOT'].quantile(0.99))
plt.show()

# DIAS_PERM by tipo_fratura
print("\nAnalysis of DIAS_PERM by Fracture Type:")
plt.figure(figsize=(14, 8))
sns.boxplot(y='tipo_fratura', x='DIAS_PERM', data=df, order=tipo_fratura_counts.index, palette='coolwarm')
plt.title('Days of Stay by Fracture Type')
plt.xlabel('Days of Stay')
plt.ylabel('Fracture Type')
plt.xlim(0, df['DIAS_PERM'].quantile(0.99))
plt.show()

# Analysis of Hospital Death (since it was 0 for all, let's reconfirm)
if df['obito_hospitalar'].sum() == 0:
    print("\nWARNING: The 'obito_hospitalar' column contains only 0 values, indicating that no hospital deaths are recorded in this dataset. This could be a data collection issue or the dataset may not capture this event.")
else:
    print("\nAnalysis of Hospital Death by Age Group:")
    obito_faixa_etaria = df.groupby('faixa_etaria_corrigida')['obito_hospitalar'].value_counts(normalize=True).unstack() * 100
    print(obito_faixa_etaria)

    plt.figure(figsize=(12, 7))
    obito_faixa_etaria.plot(kind='bar', stacked=True, colormap='Accent')
    plt.title('Proportion of Hospital Death by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Proportion (%)')
    plt.xticks(rotation=45)
    plt.legend(title='Hospital Death', labels=['No', 'Yes'])
    plt.show()


    --- Detailed Statistical Analysis ---

Analysis of the 'SEXO' Variable:
                Count  Proportion (%)
Female         227783       64.661665
Male           124486       35.338335

Analysis of the 'MORTE' Variable:
       Count  Proportion (%)
No    342905       97.341804
Yes     9364        2.658196

Analysis of the 'faixa_etaria_corrigida' Variable:
                   Count  Proportion (%)
60-69 years       106062       30.108241
70-79 years        98669       28.009561
80-89 years        81949       23.263188
90+ years          22981        6.523708
Below 60 years     42608       12.095302

Analysis of the 'tipo_fratura' Variable:
                   Count  Proportion (%)
Proximal femur    175183       49.729894
Forearm/Wrist     119599       33.951043
Humerus            46348       13.156991
Vertebra            7673        2.178165
Hip/Pelvis          3466        0.983907

Analysis of the 'regiao' Variable:
                  Count  Proportion (%)
Not classified   352269           100.0

Analysis of the 'tem_osteoporose' Variable:
   Count  Proportion (%)
0 352179       99.974451
1     90        0.025549

Analysis of the 'obito_hospitalar' Variable:
   Count  Proportion (%)
0 352269           100.0

Analysis of the 'ano_internacao' Variable:
       Count  Proportion (%)
2019   77373       21.964181
2020   80127       22.745970
2021   89004       25.265919
2023  105765       30.023931

Analysis of the 'IDADE' Variable:
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

Analysis of the 'VAL_TOT' Variable (Total Hospitalization Cost):
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

Analysis of the 'DIAS_PERM' Variable (Original Days of Stay):
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

Analysis of the 'DIAS_INTERNACAO' Variable (Calculated Hospitalization Days):
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

--- Correlation between Numerical Variables ---
Correlation Matrix:
                       IDADE   VAL_TOT  DIAS_PERM  DIAS_INTERNACAO  munResLat  munResLon  munResAlt  munResArea
IDADE            1.000000  0.297587   0.249131         0.245680  -0.149755   0.020971   0.060588   -0.068444
VAL_TOT          0.297587  1.000000   0.475463         0.468795  -0.082131   0.010429   0.022640   -0.037425
DIAS_PERM        0.249131  0.475463   1.000000         0.988911  -0.010547   0.076020  -0.082090    0.000782
DIAS_INTERNACAO  0.245680  0.468795   0.988911         1.000000  -0.010907   0.074873  -0.079594    0.000562
munResLat       -0.149755 -0.082131  -0.010547        -0.010907   1.000000   0.467383  -0.338821    0.160748
munResLon        0.020971  0.010429   0.076020         0.074873   0.467383   1.000000  -0.228519   -0.235924
munResAlt        0.060588  0.022640  -0.082090        -0.079594  -0.338821  -0.228519   1.000000   -0.065446
munResArea      -0.068444 -0.037425   0.000782         0.000562   0.160748  -0.235924  -0.065446    1.000000

Analysis of VAL_TOT by SEXO:

Analysis of DIAS_PERM by SEXO:

Analysis of VAL_TOT by Age Group:

Analysis of DIAS_PERM by Age Group:

Analysis of VAL_TOT by Fracture Type:

Analysis of DIAS_PERM by Fracture Type:
