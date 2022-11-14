#%%

import os
from re import search, IGNORECASE

root_dir = r"/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/sequences2"
proteins = []
pattern = ['original', 'prediction']

for file in os.scandir(root_dir):
    if search(r'|'.join(pattern), str(file), IGNORECASE):
        proteins.append(file.name.split('_')[1].split(".")[0])

for protein in proteins:
    id_count = (proteins.count(protein))
    if id_count != 2:
        print(f"{protein} is found {id_count} times")
print(len(proteins))

#%%
for folder, subfolders, files in os.walk(root_dir):
    for f in files:
        if search(r'|'.join(pattern), str(file), IGNORECASE):
            protein_name = f.split('_')[1].split(".")[0]
            seq_type = f.split('_')[0]
            print(f'file is {f} and name is {protein_name} and type is {seq_type}')
            # print(f"New name is", os.path.join(folder, f"{protein_name}_{seq_type}.fasta")
            os.rename(os.path.join(folder, f), os.path.join(folder, f"{protein_name}_{seq_type}.fasta"))




# 3648
# Store is found 1 times
# 1JKOC is found 1 times - no predicted sequence so I deleted it

