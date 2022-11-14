# load required packages
library(tidyverse)
library(gt)
library(gtExtras)

# read in data
setwd('/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/03_substitution_matrix')
log_odds_matrix <- read_csv2('logoddsmatrix.csv') 
pam40_matrix <- read_csv2('pam40.csv')

# convert column 1 to rowname
log_odds_matrix <- log_odds_matrix %>% 
  column_to_rownames('...1')

pam40_matrix <- pam40_matrix %>% 
  column_to_rownames('...1')

# reorder amino acids to follow Dayhoff classification scheme
log_odds_matrix <- log_odds_matrix[, c('C', 'S', 'T', 'A', 'G','P', 'D', 'E', 
                                       'Q', 'N', 'H', 'R', 'K', 'M', 'I', 'L', 
                                       'V', 'W', 'Y', 'F')]
log_odds_matrix <- log_odds_matrix[c('C', 'S', 'T', 'A', 'G','P', 'D', 'E', 
                                     'Q', 'N', 'H', 'R', 'K', 'M', 'I', 'L', 
                                     'V', 'W', 'Y', 'F'), ]

pam40_matrix <- pam40_matrix[, c('C', 'S', 'T', 'A', 'G','P', 'D', 'E', 
                                 'Q', 'N', 'H', 'R', 'K', 'M', 'I', 'L', 
                                 'V', 'W', 'Y', 'F')]
pam40_matrix <- pam40_matrix[c('C', 'S', 'T', 'A', 'G','P', 'D', 'E', 
                               'Q', 'N', 'H', 'R', 'K', 'M', 'I', 'L', 
                               'V', 'W', 'Y', 'F'), ]

# export to Python 
p <- pam40_matrix %>% 
  rownames_to_column('22')
write.csv(p, 'pam_matrix')
l <- log_odds_matrix %>% 
  rownames_to_column('22')
write.csv(l, 'logodds_matrix')


# get results back into r from pandas corr
together <- read_csv2('correlation_values_pam40_vs_sub_counts.csv')

# Visualise correlation as a gt table, coloured by value
correlation_values_tables <- together %>% 
  gt() %>%
  data_color(
    columns = 2:3,
    colors = scales::col_numeric(
      palette = c("purple", 'white', "green"),
      domain = c(-1, 1)
    )) %>% 
  fmt_number(columns = 2:3,decimals = 2) %>% 
  cols_align(align = 'center', columns = 'Amino Acid') %>% 
  tab_header(title = 'Correlation',
             subtitle = 'PAM40 vs SeqPredNN')

# save table for report
correlation_values_tables %>% 
  gtsave(filename='correlation_values_tables.docx')

# Visualise Log Odds Matrix
rounded_matrix <- as.matrix(round(log_odds_matrix, 1))

rounded_matrix_table <-  rounded_matrix %>% 
  as.data.frame() %>% 
  gt(rownames_to_stub = TRUE) %>% 
  data_color(
    columns = everything(),
    colors = scales::col_numeric(
      palette = c("purple", 'white', "green"),
      domain = c(-4, 4)
    ))

# save table for report
rounded_matrix_table %>% 
  gtsave(filename='rounded_matrix_table.docx')
