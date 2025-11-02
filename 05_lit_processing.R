# R script: MDR-TB BPaLM HTA – literature processing
# install.packages(c("tidyverse","readr"))
library(tidyverse)
refs <- read_csv("data/mdrtb_bpalm_search_results.csv")
refs_clean <- refs %>% distinct(title, .keep_all = TRUE)
write_csv(refs_clean, "output/mdrtb_bpalm_screening_sheet.csv")
