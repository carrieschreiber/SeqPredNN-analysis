# %%
""" Gets only the original and predicted sequences """
import os
from shutil import copy

root_dir = r"/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/SeqPredNN_Predictions"  # 1826 proteins
dest_dir = r"/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/sequences"  # 3647 files = 5 files missing? should be 3652

for folder, subfolders, files in os.walk(root_dir):
    if folder != root_dir:
        for f in files:
            if f.endswith(".txt") and f != 'report.txt':
                os.rename(os.path.join(folder, f),
                          os.path.join(folder, f"{os.path.splitext(f)[0]}_{os.path.basename(folder)}.fasta"))

for folder, subfolders, files in os.walk(root_dir):
    if folder != root_dir:
        for f in files:
            if f.endswith(".fasta"):
                copy(os.path.join(folder, f), os.path.join(dest_dir, f))
