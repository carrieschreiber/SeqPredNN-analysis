#%% Importing packages and data

from Bio import SeqUtils
import pandas as pd
import pyperclip
amino_acids = SeqUtils.IUPACData.protein_letters



df = pd.read_csv("/Users/carolineschreiber/PycharmProjects/analysis-of-designed-proteins/data/02_results/results_30_09.csv")

original = df.query('seq_type == "original"')['sequence']
predicted = df.query('seq_type == "predicted"')['sequence']

joined_original = ''.join(original)
joined_predicted = ''.join(predicted)

print(len(joined_predicted))
print(len(joined_original))
#%% Setting up the data structure

substitution_counts = []

for first_aa in amino_acids:
    for second_aa in amino_acids:
        substitution_counts.append([first_aa, second_aa, 0])

print(substitution_counts)
print(len(substitution_counts))

#%%
for original_aa, predicted_aa in zip(joined_original, joined_predicted):
    for index, (first, second, number) in enumerate(substitution_counts):
        if original_aa == first and predicted_aa == second:
            print(f"original = {original_aa}, first = {first}")
            print(f"predicted = {predicted_aa}, second = {second}")
            substitution_counts[index][2] = substitution_counts[index][2] + 1
            print(substitution_counts[index][2])

#%%
print(*substitution_counts, sep="\n")


#%% Validation that substitution numbers add up to sequence length

count = 0

for index, (first, second, number) in enumerate(substitution_counts):
    count += number

print(len(joined_original))
print(len(joined_predicted))
print(count)

#%%

print(substitution_counts)

#%%
df = (pd.DataFrame(substitution_counts, columns=['original_aa', 'predicted_aa', 'count']))

df.to_csv('substitution_counts_2_nov.csv', index=False)