#%%
import pandas as pd

original_df = pd.read_csv("final_df.csv")
#%%
print(original_df)
#%%
count = 0
for row in original_df.iterrows():
    seq = str(original_df.sequence)
    if 'X' in seq:
        count += 1
print(count)

