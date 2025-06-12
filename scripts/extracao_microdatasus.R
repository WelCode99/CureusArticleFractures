# -----------------------------------------------------------------------------
# Script de Extração e Pré-processamento de Dados de Fraturas do SIH-DATASUS
# -----------------------------------------------------------------------------
# Objetivo: Baixar e processar dados de internações por fraturas de fragilidade
#           entre 2019 e 2023, gerando o arquivo dados/Fraturas.csv.
# Dependências: microdatasus, dplyr, readr
# -----------------------------------------------------------------------------

# 1. Instalação / Carregamento de Pacotes -------------------------------------
if (!require("microdatasus")) install.packages("microdatasus")
if (!require("dplyr"))       install.packages("dplyr")
if (!require("readr"))       install.packages("readr")

library(microdatasus)
library(dplyr)
library(readr)

# 2. Parâmetros de Extração ----------------------------------------------------
anos_de_interesse <- 2019:2023
sistema_info      <- "SIH-RD"   # RD = Reduzida

# 3. Download e Processamento --------------------------------------------------
lista_dados_fraturas <- list()

for (ano in anos_de_interesse) {
  for (mes in 1:12) {
    mes_formatado <- sprintf("%02d", mes)
    message(paste(">> Extração:", mes_formatado, "/", ano))

    tryCatch({
      dados_brutos <- fetch_datasus(year_start = ano, month_start = mes,
                                    year_end = ano, month_end = mes,
                                    information_system = sistema_info)
      dados_processados <- process_sih(dados_brutos)

      # 4. Filtragem por CIDs --------------------------------------------------
      cids_fraturas <- c("S72", "S52", "S42", "S62", "S22", "S32")
      dados_filtrados <- dados_processados %>%
        filter(substr(DIAG_PRINC, 1, 3) %in% cids_fraturas)

      if (nrow(dados_filtrados) > 0) {
        lista_dados_fraturas[[paste(ano, mes_formatado, sep = "_")]] <- dados_filtrados
        message(">> Adicionado.")
      }

    }, error = function(e) {
      message(paste("!! Falha:", mes_formatado, "/", ano, "->", e$message))
    })
  }
}

# 5. Consolidação --------------------------------------------------------------
if (length(lista_dados_fraturas) > 0) {
  dados_fraturas_final <- bind_rows(lista_dados_fraturas)
  dir.create("../dados", showWarnings = FALSE)
  write_csv(dados_fraturas_final, "../dados/Fraturas.csv")
  message("Arquivo '../dados/Fraturas.csv' criado com sucesso!")
  message(paste("Total de registros:", nrow(dados_fraturas_final)))
  print(head(dados_fraturas_final))
} else {
  message("Nenhum dado extraído.")
}
