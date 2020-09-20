from typing import Dict
import os
from string import ascii_letters

from Name import NameDefinition, Gender, Region

import csv

from file_utils import save_names, name_dict_to_dataframe

names_csv_filename = os.path.join("name_lists", "names_merged.csv")
output_filename = "names_output.csv"

religious_indicators = ["lord", "god", "goddess", "zeus", "virgin"]
bad_name_endings = ('a', 'i')

english_origins = [Region.United_States, Region.United_Kingdom, Region.English]
indian_origins = [Region.Tamil, Region.Malayalam, Region.Sanskrit, Region.Telugu, Region.Muslim, Region.Bengali,
                  Region.Marathi, Region.Punjabi]


def exclude_names_ending_in(names: Dict[str, NameDefinition]):
    included_names = {}

    for n in names:
        name_def = names[n]
        likely_indian = any(o in indian_origins for o in name_def.origin)
        if not likely_indian:
            included_names[n] = name_def
        elif not name_def.name.endswith(bad_name_endings):
            included_names[n] = name_def

    print(f"Removed {len(names.keys()) - len(included_names.keys())} Indian names ending in {bad_name_endings}")
    return included_names


def exclude_hyphenated_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if not '-' in name_def.name:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names because they contained a hyphen ('-')")
    return included_names


def exclude_nonlatin_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        if all(c in ascii_letters for c in n):
            included_names[n] = names[n]
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names because they contained non-latin characters")
    return included_names


def exclude_apostrophe_names(names: Dict[str, NameDefinition]):
    included_names = {}
    apostrophes = ['\'', '’']
    for n in names:
        name_def = names[n]
        contains_apostrophe = False
        for a in apostrophes:
            if a in name_def.name:
                contains_apostrophe = True
        if not contains_apostrophe:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names because they contained an apostrophe (')")
    return included_names


def exclude_boy_names(names: Dict[str, NameDefinition]) -> Dict[str, NameDefinition]:
    included_names = {}
    for n in names:
        name_def = names[n]
        if name_def.gender != Gender.boy:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} boy names")
    return included_names


def exclude_meta_names(names: Dict[str, NameDefinition]) -> Dict[str, NameDefinition]:
    alias_indicators = ['variant of ', 'variation of ', 'diminutive of ', 'abbreviation of ', 'derived from ',
                        'surname']
    included_names = {}
    for n in names:
        likely_an_alias = False
        name_def = names[n]
        for indicator in alias_indicators:
            if indicator in name_def.get_meaning().lower():
                likely_an_alias = True
        if not likely_an_alias:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} meta-names")
    return included_names


def exclude_meaningless_names(names: Dict[str, NameDefinition]) -> Dict[str, NameDefinition]:
    included_names = {}
    for n in names:
        name_def = names[n]
        if name_def.get_meaning():
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names with no meaning")
    return included_names


def exclude_muslim_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if [Region.Muslim] != name_def.origin:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} Muslim names")
    return included_names


def exclude_religious_meanings(names: Dict[str, NameDefinition]):
    accepted_names = {}
    for n in names:
        name_def = names[n]
        likely_religious = False
        if name_def is None:
            continue
        for word in religious_indicators:
            if word in name_def.get_meaning().lower():
                likely_religious = True
        if not likely_religious:
            accepted_names[n] = names[n]
    print(f"Removed {len(names.keys()) - len(accepted_names.keys())} religious names")
    return accepted_names


def read_names_csv(filename: str) -> Dict[str, NameDefinition]:
    names = {}
    with open(filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        number_merged = 0
        for row in csvreader:
            if row['name'] in names and names[row['name']] is not None:
                existing_name = names[row['name']]
                existing_name.append_attrs(gender=Gender.from_str(row['gender']),
                                           meaning=row['meaning'],
                                           origin=row['origin'])
                names[row['name']] = existing_name
                number_merged = number_merged + 1
            else:
                names[row['name']] = NameDefinition(name=row['name'],
                                                    gender=Gender.from_str(row['gender']),
                                                    meaning=row['meaning'],
                                                    origin=row['origin'])
        print(f"merged {number_merged} names")
    return names


def apply_filters(names_dict: Dict[str, NameDefinition]):
    filtered_names = names_dict
    # filtered_names = exclude_names_ending_in(filtered_names)
    # filtered_names = exclude_nonlatin_names(filtered_names)
    # filtered_names = exclude_hyphenated_names(filtered_names)
    # filtered_names = exclude_meta_names(filtered_names)
    # filtered_names = exclude_religious_meanings(filtered_names)
    # filtered_names = exclude_boy_names(filtered_names)
    # filtered_names = exclude_muslim_names(filtered_names)
    filtered_names = exclude_meaningless_names(filtered_names)
    print(f"filtered a total of {len(names_dict.keys()) - len(filtered_names.keys())} names")
    return filtered_names


def name_stats(names_dict: Dict[str, NameDefinition]):
    english_count = 0
    indian_count = 0
    for name in names_dict:
        origins = names_dict[name].origin
        likely_indian = any(o in indian_origins for o in origins)
        likely_english = any(o in english_origins for o in origins)
        if likely_indian:
            indian_count = indian_count + 1
        if likely_english:
            english_count = english_count + 1
    print(f"Counted {indian_count} Indian names and {english_count} English names")


def main():
    names_dict = read_names_csv(names_csv_filename)
    name_stats(names_dict)
    names_dict = apply_filters(names_dict)

    names_dataframe = name_dict_to_dataframe(names_dict)
    save_names(output_filename, names_dataframe)


main()
