library(tidyverse)

df <- read_csv('results/final_df.csv')

no_x_df <- df %>% 
  filter(!grepl('X', df$sequence))

write_csv(no_x_df, "no_x_df.csv")

no_x_df %>% 
  group_by(name) %>% 
  count() %>% 
  filter(n == 1) %>% 
  select(name) %>% 
  clipr::write_clip()

updated_df <- read_csv2('results/no_x_df.csv')

updated_df %>% 
  filter(grepl('X', updated_df$sequence))

no_x_df
updated_df
