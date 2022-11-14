import argparse
import zipfile
import pathlib
import pandas as pd
import numpy as np


def get_args():
    arg_parser = argparse.ArgumentParser(description="access zipped ColabFold results")
    arg_parser.add_argument('-i', '--input_dir', type=str, help="input directory containing zipped results")
    args = arg_parser.parse_args()
    return pathlib.Path(args.input_dir)


def get_seq_counts():
    names_list = []
    seq_type_list = []
    num_of_seqs_list = []

    for initial_file in input_dir.glob('*.result.zip'):

        with zipfile.ZipFile(initial_file, "r") as f:
            for name in f.namelist():
                if name.endswith(".a3m"):
                    data = f.read(name).decode().splitlines()
                    count = 0
                    for line in data:
                        if line[0] == ">":
                            count += 1
                    filename = name.replace('original_sequence_', "").replace('prediction_', "")
                    names_list.append(filename.split("_")[0])
                    num_of_seqs_list.append(count)

                    if 'original' in name:
                        seq_type_list.append('original')
                    else:
                        seq_type_list.append('predicted')

                    seqs_df = pd.DataFrame(
                        np.column_stack([names_list, seq_type_list, num_of_seqs_list]),
                        columns=['name', "seq_type", 'num_of_seqs'])

    return seqs_df


if __name__ == "__main__":
    input_dir = get_args()

    num_of_seqs_df = get_seq_counts()

    batch_number = input_dir.name.split("batch_")[1].replace("_output", "")
    num_of_seqs_df['batch_number'] = batch_number
    num_of_seqs_df.to_csv(f"results_alignment_{batch_number}.csv", index=False)
