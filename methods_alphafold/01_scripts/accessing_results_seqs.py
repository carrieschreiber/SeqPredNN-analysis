import argparse
import pathlib
import pandas as pd
import numpy as np


def get_args():
    arg_parser = argparse.ArgumentParser(description="access original fasta sequences")
    arg_parser.add_argument('-i', '--input_dir', type=str, help="input directory containing fasta files")
    args = arg_parser.parse_args()
    return pathlib.Path(args.input_dir)


def get_seq():
    names_list = []
    seq_type_list = []
    fasta_seq_list = []
    for file in input_dir.iterdir():
        if file.name.endswith('.fasta'):

            filename = file.name.replace("_prediction", "").replace("_original", "").replace(".fasta", "")
            names_list.append(filename)

            with open(file, 'r+') as f:
                content = f.readlines()
                fasta_seq = content[1]
                fasta_seq_list.append(fasta_seq)

            if 'original' in file.name:
                seq_type_list.append('original')
            else:
                seq_type_list.append('predicted')

            fasta_df = pd.DataFrame(
                np.column_stack([names_list, seq_type_list, fasta_seq_list]),
                columns=['name', "seq_type", 'sequence'])
    return fasta_df


if __name__ == "__main__":
    input_dir = get_args()
    df = get_seq()

    batch_number = input_dir.name.split("batch_")[1].replace("_output", "")
    df['batch_number'] = batch_number
    df.to_csv(f"results_fasta_{batch_number}.csv", index=False)
