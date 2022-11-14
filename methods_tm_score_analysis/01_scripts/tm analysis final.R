#tm scoring 8 nov

library(tidyverse)
library(ggpubr)

# reading in data ---------------------------------------------------------
setwd('/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/methods/05_tm_score_analysis')

tm_df <- read_csv('02_results/tm_score_output.csv') 

main_df <- read_csv('/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/data/02_results/results_30_09.csv') %>% 
  janitor::clean_names()

tm_df <- tm_df %>% 
  dplyr::rename(name = protein)

joined <- main_df %>%
  inner_join(tm_df, by = c('name' = 'name', 'seq_type' = 'seq_type'))

main_df %>% 
  ggplot(aes(x=ptm)) +
  geom_histogram() +
  facet_grid(rows = vars(seq_type)) +
  theme_bw()

tm_df %>% 
  ggplot(aes(x=tm_score)) +
  geom_histogram() +
  facet_grid(rows = vars(seq_type)) +
  theme_bw()

# 396 parsed correctly
all_common_residues <- joined %>% 
  mutate(difference = seq_length - common_residues) %>% 
  filter(difference < 1)

all_common_residues %>% 
  arrange(seq_length)

correlation <- ggscatter(all_common_residues, x = "tm_score", y = "ptm", facet.by = 'seq_type',
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "actual TM score", ylab = "AlphaFold pTM", color='seq_type') +
  labs(title='Correlation between TM score and pTM') +
  theme_bw() +
  theme(legend.position = 'none')

ggsave('correlation_tm_scores.png', correlation, device = 'png', dpi=600)

ggscatter(all_common_residues, x = "tm_score", y = "ptm",
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "actual TM score", ylab = "AlphaFold pTM", color='seq_type') +
  labs(title='Correlation between TM score and pTM') +
  theme_bw() +
  theme(legend.position = 'none')
