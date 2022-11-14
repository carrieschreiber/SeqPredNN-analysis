#%%
from Bio.PDB import PDBParser, PDBList
import pandas as pd

parser = PDBParser()
pdb_list = PDBList()

id_txt_path = '/protein_and_chain_ids'
dir_path = '/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/pdb_files'

#%%
ids = pd.read_csv(id_txt_path)
protein_ids = list(ids['protein_id'])

#%%
for index, value in enumerate(protein_ids):
    print(f"Started on number {index + 1} out of 1107, chain ID {value}")
    pdb_list.retrieve_pdb_file(pdb_code=value, file_format='pdb', pdir=dir_path)
    print(f"Finished number {index + 1} out of 1107, chain ID {value}")




