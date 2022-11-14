# %%
import numpy as np
import pandas as pd
import argparse
import pathlib
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from statistics import median


def get_args():
    arg_parser = argparse.ArgumentParser(description="calculate ProtParam properties of protein sequences")
    arg_parser.add_argument('-i', '--input_dir', type=str, help="input directory containing fasta sequences")
    args = arg_parser.parse_args()
    return pathlib.Path(args.input_dir)


def get_protparam_results():
    names_list = []
    seq_type_list = []

    molecular_weight_list = []
    aromacity_list = []
    instability_list = []
    gravy_list = []
    isoelectric_list = []

    for file in input_dir.iterdir():
        if file.name.endswith('.fasta'):
            filename = file.name.replace('prediction_', "").replace('original_', "").replace('.fasta', "")

            names_list.append(filename)

            if 'original' in file.name:
                seq_type_list.append('original')
            else:
                seq_type_list.append('predicted')

            with open(file, "rb") as f:
                data = f.read().decode().splitlines()
                fasta_seq = data[1]

            seq = ProteinAnalysis(fasta_seq)

            # metrics
            molecular_weight_list.append(seq.molecular_weight())
            aromacity_list.append(seq.aromaticity())
            instability_list.append(seq.instability_index())
            gravy_list.append(seq.gravy())
            isoelectric_list.append(seq.isoelectric_point())

        protparam_dataframe = pd.DataFrame(
            np.column_stack(
                [names_list, seq_type_list, molecular_weight_list, aromacity_list, instability_list, gravy_list,
                 isoelectric_list]),
            columns=['name', 'seq_type', 'molecular_weight', 'aromacity', 'instability', 'gravy', 'isoelectric'])

    return protparam_dataframe


if __name__ == "__main__":
    input_dir = get_args()

    protparam_df = get_protparam_results()
    protparam_df.to_csv('results_with_protparam.csv', index=False)
