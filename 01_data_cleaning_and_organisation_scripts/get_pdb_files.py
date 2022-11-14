from os import scandir
from re import findall, IGNORECASE

source_file_path = "/apps/PDB/pdb/all"

with open('pdb_ids.txt') as f:
    pdb_ids = f.read().splitlines()

protein_ids = {x[:4] for x in pdb_ids}

final_files = []

for filename in scandir(source_file_path):
    if any(findall(r'|'.join(protein_ids), str(filename), IGNORECASE)) and filename not in final_files:
        final_files.append(filename.path)

with open('pdb_filenames.txt', 'w') as f:
    f.write('\n'.join(final_files))

print(f'The number of files found is {len(final_files)}')  # 1849 (out of 1891) = 42 missing PDB files from HPC


