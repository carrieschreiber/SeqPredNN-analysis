import numpy as np
import pandas as pd
import argparse
import zipfile
import pathlib
import json
import statistics


def get_args():
    arg_parser = argparse.ArgumentParser(description="access zipped ColabFold results")
    arg_parser.add_argument('-i', '--input_dir', type=str, help="input directory containing zipped results")
    args = arg_parser.parse_args()
    return pathlib.Path(args.input_dir)


def get_pae_metrics():
    names_list = []
    seq_type_list = []
    seq_length_list = []

    # PAE metrics
    highest_possible_pae_list = []
    max_pae_list = []
    min_pae_list = []
    median_pae_list = []

    for initial_file in input_dir.glob('*.result.zip'):
        with zipfile.ZipFile(initial_file, "r") as x:
            for name in x.namelist():
                if '_rank_1_' in name and name.endswith(".json"):
                    json_file = x.read(name)
                    content = json.loads(json_file)
                    filename = name.replace('original_sequence_', "").replace('prediction_', "")
                    names_list.append(filename.split("_")[0])

                    if 'original' in name:
                        seq_type_list.append('original')
                    else:
                        seq_type_list.append('predicted')

                    seq_length_list.append(len(content['plddt']))

                    # PAE metrics
                    highest_possible_pae_list.append(content['max_pae'])
                    max_pae_list.append(max((max(i) for i in content['pae'])))
                    min_pae_list.append(min((min(i) for i in content['pae'])))
                    median_pae_list.append(statistics.median((statistics.median(i) for i in content['pae'])))

                    pae_dataframe = pd.DataFrame(
                        np.column_stack([names_list, seq_type_list, seq_length_list, highest_possible_pae_list,
                                         max_pae_list, min_pae_list, median_pae_list]),
                        columns=['name', "seq_type", 'seq_length', 'highest_possible_pae', 'max_pae',
                                 'min_pae', 'median_pae'])

    return pae_dataframe


def get_ptm_and_plddt_metrics():
    names_list = []
    seq_type_list = []

    # pTM metrics
    ptm_list = []

    # pLDDT metrics
    median_plddt_list = []
    max_plddt_list = []
    min_plddt_list = []
    std_plddt_list = []
    var_plddt_list = []
    q1_plddt_list = []
    q3_plddt_list = []

    for initial_file in input_dir.glob('*.result.zip'):
        with zipfile.ZipFile(initial_file, "r") as x:
            for name in x.namelist():
                if '_rank_1_' in name and name.endswith(".json"):
                    json_file = x.read(name)
                    content = json.loads(json_file)
                    filename = name.replace('original_sequence_', "").replace('prediction_', "")
                    names_list.append(filename.split("_")[0])

                    if 'original' in name:
                        seq_type_list.append('original')
                    else:
                        seq_type_list.append('predicted')

                    # pTM metrics
                    ptm_list.append(content['ptm'])

                    # pLDDT metrics
                    max_plddt_list.append(max(content['plddt']))
                    min_plddt_list.append(min(content['plddt']))
                    std_plddt_list.append(statistics.stdev(content['plddt']))
                    var_plddt_list.append(statistics.variance(content['plddt']))

                    quantile = statistics.quantiles(content['plddt'])
                    q1_plddt_list.append(quantile[0])
                    median_plddt_list.append(quantile[1])
                    q3_plddt_list.append(quantile[2])

                    plddt_dataframe = pd.DataFrame(
                        np.column_stack([names_list, seq_type_list, ptm_list, max_plddt_list, min_plddt_list,
                                         std_plddt_list, var_plddt_list, q1_plddt_list,
                                         median_plddt_list, q3_plddt_list]),
                        columns=['name', 'seq_type', 'ptm', 'max_plddt', 'min_plddt', 'std_plddt',
                                 'var_plddt', 'q1_plddt', 'median_plddt', 'q3_plddt'])

    return plddt_dataframe


if __name__ == "__main__":
    input_dir = get_args()

    pae_df = get_pae_metrics()
    plddt_df = get_ptm_and_plddt_metrics()

    json_results_df = pd.merge(pae_df, plddt_df, on=['name', 'seq_type'])

    batch_number = input_dir.name.split("batch_")[1].replace("_output", "")
    json_results_df['batch_number'] = batch_number

    json_results_df.to_csv(f"results_json_{batch_number}.csv", index=False)
