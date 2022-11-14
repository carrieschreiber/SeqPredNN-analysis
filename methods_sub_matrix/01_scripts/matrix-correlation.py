#%%
import pandas as pd
import numpy as np

pam_df = pd.read_csv('/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/methods/03_substitution_matrix/pam_matrix', index_col=0)
log_odds_df = pd.read_csv('/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/methods/03_substitution_matrix/new_matrix.csv', index_col=0)

log_odds_df

#%%

print(pam_df.shape)

print(log_odds_df.shape)


#%%

# column wise correlation
pam_df.corrwith(log_odds_df, axis=1, method='spearman')

#%%
# row wise correlation
pam_df.corrwith(log_odds_df, axis=0, method='spearman')