library(tidyverse)
library(Biostrings)
library(stringr)

updated_df <- read_csv2('results/no_x_df.csv')

updated_df <- updated_df %>% 
  mutate(protein_id = str_sub(name, 1, 4)) %>% 
  mutate(chain_id = str_sub(name, -1))

sequence_similarity <- function(original_seq, predicted_seq) {
  alignment <- Biostrings::pairwiseAlignment(original_seq, predicted_seq)
  similarity_percentage <- Biostrings::pid(alignment, type="PID3")
}

grouped_and_arranged <- updated_df %>%
  group_by(name) %>% 
  arrange(name, seq_type) %>% 
  mutate(group_id = cur_group_id()) %>% 
  select(group_id, everything())

empty_list <- vector(mode = "list", length = 1367)

for (i in (1:1367)) {
  temp_df <- grouped_and_arranged %>% 
    filter(group_id == i)
  
  original <- temp_df[1,]$sequence
  predicted <- temp_df[2,]$sequence
  
  empty_list[i] <- sequence_similarity(original, predicted)
  
  
}
  
seq_similarity <- as_tibble_col(empty_list, column_name = "value") %>% 
  unnest(value) %>% 
  mutate(group_id = row_number())

arranged_updated <- grouped_and_arranged %>% 
  left_join(seq_similarity) %>% 
  select(value, everything()) %>% 
  ungroup()

updated_df <- arranged_updated %>% 
  mutate(similarity = value) %>% 
  select(-value) %>% 
  select(group_id, name, protein_id, chain_id, everything())

write_csv(updated_df, "df_with_similarity.csv")

names(updated_df) %>% 
  clipr::write_clip()


