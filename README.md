# Repositório de Dados e Código para o Artigo [TÍTULO DO ARTIGO]

[![DOI](https://zenodo.org/badge/1000939241.svg)](https://doi.org/10.5281/zenodo.15650904)

Este repositório contém os dados e o código de análise para o artigo intitulado "[TÍTULO DO ARTIGO]" submetido à revista Cureus.

## Descrição

[INSIRA AQUI UMA BREVE DESCRIÇÃO DO ESTUDO, SEUS OBJETIVOS E MÉTODOS.]

## Estrutura do Repositório

- **/dados**: Contém o conjunto de dados utilizado na análise.
  - `FraturasCorrigido.csv`: O conjunto de dados processados.
  - `Fraturas.csv`: Conjunto de dados bruto extraído do DATASUS (gerado pelo script R).
- **/scripts**: Contém os scripts de extração e análise.
  - `extracao_microdatasus.R`: Script R para extrair e pré-processar dados do SIH-DATASUS.
  - `analise.py`: Script Python para realizar a análise descritiva e gerar os gráficos.
- **/documentos**: Contém documentos suplementares.
  - `ResultadosDaAnaliseArtigo.pdf`: PDF com os resultados detalhados da análise.
  - `document.pdf`: Manuscrito do artigo.
  - `Código inicial de analise 20b1cce9e5718010aafeedd9b99b64b7.md`: Código original da análise.
  - `Differential Mortality Risk and Healthcare Costs Associated with Fragility Fracture Types.docx`: Manuscrito do artigo (formato DOCX).

## Como Reproduzir a Análise

### Pré-requisitos

- Python 3.8 ou superior.
- R 4.0 ou superior (apenas se desejar executar a extração de dados do DATASUS).
- As bibliotecas Python listadas no arquivo `requirements.txt`.
- Pacotes R: microdatasus, dplyr, readr (apenas para extração).

### Passos para Execução

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/WelCode99/CureusArticleFractures.git
    cd CureusArticleFractures
    ```

2.  **Para análise Python:**

    a. Crie e ative um ambiente virtual (altamente recomendado):

    ```bash
    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

    b. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

    c. Execute o script de análise:

    ```bash
    python scripts/analise.py
    ```

    Os gráficos gerados pela análise serão exibidos na tela durante a execução do script.

3.  **Para extração dos dados do DATASUS (opcional):**

    Este passo é necessário apenas se você desejar recriar o conjunto de dados a partir das fontes originais.

    ```bash
    # No R ou RStudio
    Rscript scripts/extracao_microdatasus.R
    ```

    Nota: Este processo pode levar várias horas, dependendo da sua conexão com a internet, pois baixa e processa dados de 60 meses (2019-2023).

## Citação dos Dados

Se você utilizar estes dados ou o código em sua pesquisa, por favor, cite o artigo original (assim que publicado) e este repositório de dados.

**Citação do Artigo:**

> Autor(es). (Ano). Título do Artigo. _Cureus_. DOI: [DOI_A_SER_ATRIBUÍDO]

**Citação do Repositório de Dados:**

> Autor(es). (Ano). Dados e Código para: "Título do Artigo" [Repositório de dados e software]. Zenodo. DOI: 10.5281/zenodo.15650904

## Licença

O código neste repositório está sob a licença MIT. Os dados estão disponibilizados sob a licença Creative Commons Attribution 4.0 International (CC-BY-4.0). Veja o arquivo `LICENSE` para mais detalhes.
