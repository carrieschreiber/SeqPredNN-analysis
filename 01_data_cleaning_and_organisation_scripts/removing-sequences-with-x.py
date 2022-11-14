#%%
import os
import pathlib
root_dir = pathlib.Path("/sequences/sequences_updated")

for file in root_dir.iterdir():
    if file.name.endswith('.fasta'):
        with open(file, 'r') as f:
            content = f.readlines()
            seq = content[1]

        if 'X' in seq:
            os.remove(file)

#%%
from re import findall, IGNORECASE

ids = ['1ODHA', '1PPJA', '1TJXA', '1W96C', '2BO4A', '2C5AA', '2CBZA', '2J3WB', '2UUZA', '2VPZA', '2W9HA', '2WNVD', '2XG5A', '3CXBB', '3FXQA', '4AK2A', '4AKFA', '4GR6A', '5NJLA', '6R1MB', '6XN8A']
for file in root_dir.iterdir():
    if file.name.endswith('.fasta') and findall(r'|'.join(ids), str(file.name), IGNORECASE):
        os.remove(file)