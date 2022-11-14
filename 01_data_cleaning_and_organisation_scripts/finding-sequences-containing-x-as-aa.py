# %%
import os
import pandas as pd
from re import search, IGNORECASE
root_dir = r"/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/sequences_all"

ids_with_X = []
type_with_X = []
# pdb_ids = []
count = 0

# for file in os.listdir(root_dir):
#     if file.endswith('.fasta'):
#         pdb_ids.append(file.replace(".fasta", "").split("_")[1])

# for i in pdb_ids:
#     if pdb_ids.count(i) != 2:
#         print(i)


for file in os.listdir(root_dir):
    if file.endswith('.fasta'):
        with open(f"{root_dir}/{file}", 'r+') as f:
            content = f.readlines()
            fasta_seq = content[1]

        x = "original" if "original" in file else "predicted"

        if 'X' in fasta_seq:
            ids_with_X.append(file.replace(".fasta", "").split("_")[1])
            type_with_X.append(x)
            count += 1

print(f'number of records with an X in them is {count}')

unmatched_Xs = []
for i in ids_with_X:
    if ids_with_X.count(i) != 2:
        unmatched_Xs.append(i)

# 21 unmatched records
print(len(unmatched_Xs))
#%%
count = 0
for file in os.listdir(root_dir):
    if file.endswith('.fasta') and search(r'|'.join(unmatched_Xs), str(file), IGNORECASE):
        with open(f"{root_dir}/{file}", 'r+') as f:
            content = f.readlines()
            fasta_seq = content[1]

        if 'X' in fasta_seq:
            count += 1
            print(file)

print(count)