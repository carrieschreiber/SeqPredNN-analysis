# %%
import os

root_dir = r"/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/sequences"

for file in os.listdir(root_dir):
    if file.endswith(".fasta"):
        new_line = f"> {file.split('.')[0]}\n"

        with open(f"{root_dir}/{file}", 'r+') as f:
            content = f.read()
            f.seek(0)
            f.write(new_line + content)

"""Rename files to original only"""

for folder, subfolders, files in os.walk(root_dir):
    for f in files:
        if f.startswith("original"):
            print(f)
            splitted = f.split('_')
            os.rename(os.path.join(folder, f), os.path.join(folder, f"original_{splitted[2]}"))
            print(f"original_{splitted[2]}")
