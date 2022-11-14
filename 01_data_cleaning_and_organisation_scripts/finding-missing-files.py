#%%

import zipfile
import pathlib

results_dir = pathlib.Path("/Users/carolineschreiber/Downloads/batch_15_output")
input_dir = pathlib.Path("/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/sequences_batched/batch_15")

input_seqs = []
output_seqs = []

for initial_file in input_dir.iterdir():
    input_seqs.append(initial_file.name.split(".")[0])

for zip_file in results_dir.glob('*.result.zip'):
    output_seqs.append(zip_file.name.split(".")[0])

#%%
for i in input_seqs:
    if i not in output_seqs:
        print(i)