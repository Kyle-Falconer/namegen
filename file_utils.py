from typing import Dict, List
import os
import pandas as pd
from pandas import DataFrame

from Name import NameDefinition


def save_names_raw(filename, names_dict, overwrite=False):
    df = pd.DataFrame.from_dict(names_dict)

    # don't add the header row if the file already exists
    need_header = True
    if os.path.isfile(filename):
        need_header = False

    mode = "a"
    if overwrite:
        need_header = True
        mode = "w"

    with open(filename, mode) as csvfile:
        df.to_csv(csvfile, header=need_header)


def save_names_csv(output_filename: str, names_dataframes: DataFrame):
    print(f"saving {len(names_dataframes)} names to {output_filename}")
    names_dataframes.to_csv(output_filename, header=True)


def save_names_json(output_filename: str, names_dataframes: DataFrame):
    print(f"saving {len(names_dataframes)} names to {output_filename}")
    names_dataframes.to_json(output_filename, orient="records")


def name_list_to_dataframe(names_list: List[NameDefinition]) -> DataFrame:
    name_data = []
    for n in names_list:
        name_data.append(n.to_dict())
    return pd.DataFrame(name_data)


def name_dict_to_dataframe(names_dict: Dict[str, NameDefinition]) -> DataFrame:
    name_data = []
    for n in names_dict:
        name_def = names_dict[n]
        if name_def is not None:
            name_data.append(name_def.to_dict())
    return pd.DataFrame(name_data)


def count_lines(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
