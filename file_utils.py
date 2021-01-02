import json
from typing import Dict, List
import os
import pandas as pd
from pandas import DataFrame

from Name import NameDefinition, Gender, NameMeaning


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
    names_dataframes.to_json(output_filename, orient="records", indent=2)


def read_names_json(filename: str) -> Dict[str, NameDefinition]:
    names = {}
    with open(filename) as jsonfile:
        data = json.load(jsonfile)
        number_merged = 0
        for record in data:
            meanings_list = []
            for m in record['meanings']:
                meanings_list.append(NameMeaning(meaning=m['meaning'], origins=m['origins']))
            if record['name'] in names and names[record['name']] is not None:
                existing_name = names[record['name']]
                existing_name.append_attrs(gender=Gender.from_str(record['gender']),
                                           meanings=meanings_list,
                                           known_persons=record['known_persons'],
                                           source=record['source'])
                names[record['name']] = existing_name
                number_merged = number_merged + 1
            else:
                names[record['name']] = NameDefinition(name=record['name'],
                                                       gender=Gender.from_str(record['gender']),
                                                       meanings=meanings_list,
                                                       known_persons=record['known_persons'],
                                                       source=record['source'])
        print(f"merged {number_merged} names")
    return names


def name_list_to_dataframe(names_list: List[NameDefinition]) -> DataFrame:
    name_data = []
    for n in names_list:
        name_data.append(n.to_dict())
    return pd.DataFrame(name_data)


def name_dict_to_dataframe(names_dict: Dict[str, NameDefinition], condensed: bool = False) -> DataFrame:
    name_data = []
    for n in names_dict:
        name_def = names_dict[n]
        if name_def is not None:
            if condensed:
                name_data.append(name_def.to_condensed_dict())
            else:
                name_data.append(name_def.to_dict())
    return pd.DataFrame(name_data)


def count_lines(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
