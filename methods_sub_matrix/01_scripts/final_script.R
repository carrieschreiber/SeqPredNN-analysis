# attaching packages ------------------------------------------------------
library(tidyverse)
library(gt)
library(gtExtras)

# reading in data ---------------------------------------------------------
sub_counts <- read_csv('substitution_counts.csv')
pam40_matrix <- read_csv2('pam40.csv')

# adding in original and predicted total amino acid counts
sub_counts_updated <- sub_counts %>% 
  rename(pure_count = count) %>%
  group_by(predicted_aa) %>%
  mutate(seqprednn_aa_count = sum(pure_count)) %>% 
  ungroup() %>% 
  group_by(original_aa) %>%
  mutate(original_aa_count = sum(pure_count)) %>%
  ungroup()

# calculating probability and log odds of each mutation event
log_odds_matrix <- sub_counts_updated %>% 
  mutate(final_prob = pure_count / original_aa_count) %>%  # Bayes Theorem
  mutate(numerator = final_prob) %>% 
  mutate(denominator = 1 - final_prob) %>% 
  mutate(odds = numerator / denominator) %>% 
  mutate(log_odds = log(odds)) %>% 
  select(original_aa, predicted_aa, log_odds) %>% 
  pivot_wider(names_from = original_aa, values_from = log_odds)

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

# visualisation -----------------------------------------------------------

# visualising log odds matrix and saving output
log_odds_matrix <- round(log_odds_matrix, 2) # for cleaner visualisation

log_odds_matrix %>% 
  as.data.frame() %>% 
  gt(rownames_to_stub = TRUE) %>% 
  data_color(
    columns = everything(),
    colors = scales::col_numeric(
      palette = c("purple", 'white', "green"),
      domain = c(-11, 11)
    )) %>% 
  gtsave(filename='final_rounded_log_odds_matrix.docx')

# reading in correlation value data from python
spearman_correlation <- read_csv2('spearman_correlation_values.csv')

# spearman correlation visualisation
spearman_table <- spearman_correlation %>% 
  gt() %>%
  data_color(
    columns = 2:3,
    colors = scales::col_numeric(
      palette = c("purple", 'white', "green"),
      domain = c(-1, 1)
    )) %>% 
  fmt_number(columns = 2:3,decimals = 2) %>% 
  cols_align(align = 'center', columns = 'aa') %>% 
  tab_header(title = 'Spearman Correlation',
             subtitle = 'PAM40 vs SeqPredNN')   

# saving to put into report
spearman_table %>% 
  gtsave(filename='spearman_table.docx')