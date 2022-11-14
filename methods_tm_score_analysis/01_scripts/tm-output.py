# %%
import pathlib
import pandas as pd
import numpy as np

# %%
input_dir = pathlib.Path('/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/methods/05_tm_score_analysis/tm_output')
count = 0
problematic_list = []
for file in input_dir.iterdir():
    with open(file) as f:
        content = f.readlines()
        if content[0][0] == 'T':
            count += 1
            print(content[0], file.name)
            problematic_list.append(file.name)

print(count)
# %%
splitted = [i.split("_")[0] for i in problematic_list]
split_count = 0
for x in splitted:
    if splitted.count(x) == 2:
        split_count += 1
print(split_count)  # there are 137 pdb files that didn't parse correctly
# %%

protein_list = []
seq_type_list = []

common_residues_list = []
rmsd_list = []

tm_score_list = []
tm_score_d0_list = []

max_sub_score_list = []
max_sub_score_d0_list = []

gdt_ts_score_list = []
gdt_ha_score_list = []

for file in input_dir.iterdir():
    with open(file) as f:
        content = f.readlines()
        if content[0][0] != 'T':
            common_residues = int(content[13].split('=')[1].lstrip().replace('\n', ''))
            rmsd = float(content[14].split('=')[1].lstrip().replace('\n', ''))

            tm_score = float(content[16].split('=')[1].strip().split()[0])
            tm_score_d0 = float(content[16].split('=')[2].strip().split(")")[0])

            max_sub_score = float(content[17].split('=')[1].strip().split()[0])
            max_sub_score_d0 = float(content[17].split('=')[2].strip().split(')')[0])

            gdt_ts_score = float(content[18].split()[1].strip())
            gdt_ha_score = float(content[19].split()[1].strip())

            protein = file.name.split(".")[0].split('_')[0]
            seq_type = file.name.split(".")[0].split('_')[1]

            protein_list.append(protein)
            seq_type_list.append(seq_type)

            common_residues_list.append(common_residues)
            rmsd_list.append(rmsd)

            tm_score_list.append(tm_score)
            tm_score_d0_list.append(tm_score_d0)

            max_sub_score_list.append(max_sub_score)
            max_sub_score_d0_list.append(max_sub_score_d0)

            gdt_ts_score_list.append(gdt_ts_score)
            gdt_ha_score_list.append(gdt_ha_score)

tm_df = pd.DataFrame(
    np.column_stack([protein_list, seq_type_list, common_residues_list, rmsd_list, tm_score_list, tm_score_d0_list,
                     max_sub_score_list, max_sub_score_d0_list, gdt_ts_score_list, gdt_ha_score_list]),
    columns=['protein', "seq_type", 'common_residues', 'rmsd', 'tm_score', 'tm_score_d0', 'max_sub_score',
             'max_sub_score_d0', 'gdt_ts_score', 'gdt_ha_score'])

tm_df.to_csv('tm_score_output.csv', index=False)