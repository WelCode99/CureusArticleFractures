# -----------------------------------------------------------------------------
# SIH-DATASUS Fracture Data Extraction and Preprocessing Script
# -----------------------------------------------------------------------------
# Objective: Download and process data on hospitalizations for fragility fractures
#            between 2019 and 2023, generating the data/Fraturas.csv file.
# Dependencies: microdatasus, dplyr, readr
# -----------------------------------------------------------------------------

# 1. Package Installation / Loading -------------------------------------
if (!require("microdatasus")) install.packages("microdatasus")
if (!require("dplyr"))       install.packages("dplyr")
if (!require("readr"))       install.packages("readr")

library(microdatasus)
library(dplyr)
library(readr)

# 2. Extraction Parameters ----------------------------------------------------
anos_de_interesse <- 2019:2023
sistema_info      <- "SIH-RD"    # RD = Reduced

# 3. Download and Processing --------------------------------------------------
lista_dados_fraturas <- list()

for (ano in anos_de_interesse) {
  for (mes in 1:12) {
    mes_formatado <- sprintf("%02d", mes)
    message(paste(">> Extracting:", mes_formatado, "/", ano))

    tryCatch({
      dados_brutos <- fetch_datasus(year_start = ano, month_start = mes,
                                    year_end = ano, month_end = mes,
                                    information_system = sistema_info)
      dados_processados <- process_sih(dados_brutos)

      # 4. Filtering by ICDs --------------------------------------------------
      cids_fraturas <- c("S72", "S52", "S42", "S62", "S22", "S32")
      dados_filtrados <- dados_processados %>%
        filter(substr(DIAG_PRINC, 1, 3) %in% cids_fraturas)

      if (nrow(dados_filtrados) > 0) {
        lista_dados_fraturas[[paste(ano, mes_formatado, sep = "_")]] <- dados_filtrados
        message(">> Added.")
      }

    }, error = function(e) {
      message(paste("!! Failed:", mes_formatado, "/", ano, "->", e$message))
    })
  }
}

# 5. Consolidation --------------------------------------------------------------
if (length(lista_dados_fraturas) > 0) {
  dados_fraturas_final <- bind_rows(lista_dados_fraturas)
  dir.create("../data", showWarnings = FALSE)
  write_csv(dados_fraturas_final, "../data/Fraturas.csv")
  message("File '../data/Fraturas.csv' created successfully!")
  message(paste("Total records:", nrow(dados_fraturas_final)))
  print(head(dados_fraturas_final))
} else {
  message("No data extracted.")
}
