import zipfile
import pathlib
import pandas as pd
from glob import glob
import shutil
import re

# %%
id_txt_path = '/protein_and_chain_ids'
ids = pd.read_csv(id_txt_path)
protein_ids = list(ids['protein_id'])
chain_ids = list(ids['chain_id'])
combined_ids = [protein_ids[i] + chain_ids[i] for i in range(len(chain_ids))]
print(*combined_ids, sep='\n')

# %%
input_dir = pathlib.Path('/Users/carolineschreiber/Library/CloudStorage/OneDrive-StellenboschUniversity/outputs_only')
output_dir = pathlib.Path(
    '/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/tm-score-analysis/alphafold_pdbs')

# %%

for initial_file in input_dir.glob('*.result.zip'):
    with zipfile.ZipFile(initial_file) as x:
        for file_name in x.namelist():
            if '_rank_1_' in name and name.endswith(".pdb"):
                print(name)
                # x.extract(member=s,path=output_dir)

# %%

for initial_file in input_dir.glob('*.result.zip'):
    with zipfile.ZipFile(initial_file) as x:
        for info in x.infolist():
            info_filename = info.filename
            if re.match(r'^.*rank_1_model_.*.pdb', info_filename):
                print(info.filename)
                x.extract(info, output_dir)


        # for named_file in x.namelist():
        # for file in glob('*_prediction_unrelaxed_rank_1_model_?.pdb'):
        #     print(file)

# r'^.rank_1_model_?.pdb$'