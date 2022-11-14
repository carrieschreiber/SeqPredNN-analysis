#%%
import pandas as pd

updated = pd.read_csv("/results_with_protparam.csv")

original = pd.read_csv("/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/results/no_x_df.csv", sep = ";")

final = updated.merge(original, how = 'inner')

final.to_csv('updated_combined_results.csv', index=False)