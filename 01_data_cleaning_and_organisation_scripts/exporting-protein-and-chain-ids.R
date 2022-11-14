library(tidyverse)

df <- read_csv('/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/results_30_09.csv')

subsert <- df %>% 
  filter(seq_type == 'original') %>% 
  select(protein_id, chain_id)

write_csv(subsert, 'protein_and_chain_ids')