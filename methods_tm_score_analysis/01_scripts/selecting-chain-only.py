#%%
from Bio.PDB import PDBParser, Select
from Bio.PDB.PDBIO import PDBIO
from os import chdir
import pandas as pd

#%%
id_txt_path = '/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/data/02_results/protein_and_chain_ids'
ids = pd.read_csv(id_txt_path)
protein_ids = list(ids['protein_id'])
chain_ids = list(ids['chain_id'])

#%%
dir_path = '/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/methods/05_tm_score_analysis/pdb_files'

chdir('/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/tm-score-analysis/chain_pdbs')

for protein, chain in zip(protein_ids, chain_ids):
    parser = PDBParser()
    pdb_file = f'/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/tm-score-analysis/pdb_files/pdb{protein.lower()}.ent'
    structure = parser.get_structure(f'{protein.lower()}', pdb_file)
    selected_chain = structure[0][chain]
    io = PDBIO()
    io.set_structure(selected_chain)
    io.save(f'{protein}{chain}.pdb')