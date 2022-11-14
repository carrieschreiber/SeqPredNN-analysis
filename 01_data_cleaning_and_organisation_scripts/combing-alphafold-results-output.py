# %%
import pandas as pd

align = pd.read_csv(
    '/combined_results_alignment.csv')  # 4
json = pd.read_csv(
    '/combined_results_json.csv')  # 16
seqs = pd.read_csv(
    '/combined_results_seqs.csv')  # 4

df = align.merge(json, how='inner')
final_df = df.merge(seqs, how='inner')

final_df.to_csv("final_df.csv", index=False)
