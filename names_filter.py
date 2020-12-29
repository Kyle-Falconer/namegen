import json
import os
from string import ascii_letters
from typing import Dict

from Name import NameDefinition, Gender, Region, NameMeaning, NameSource
from file_utils import read_names_json, name_dict_to_dataframe, save_names_json
from name_constants import bad_name_endings, hard_to_pronounce, excluded_startings, western_origins, indian_origins, \
    religious_indicators
from name_utils import name_stats

names_json_filename = os.path.join("name_lists", "names_merged.json")
output_filename = "names_output.json"


def exclude_names_starting_in(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if not name_def.name.lower().startswith(excluded_startings):
            included_names[n] = name_def

    print(f"Removed {len(names.keys()) - len(included_names.keys())} names starting in {excluded_startings}")
    return included_names


def exclude_names_ending_in(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if not name_def.name.lower().startswith(bad_name_endings):
            included_names[n] = name_def

    print(f"Removed {len(names.keys()) - len(included_names.keys())} names ending in {bad_name_endings}")
    return included_names


def exclude_hard_to_pronounce_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        name_is_ok = True
        for phoneme in hard_to_pronounce:
            if phoneme in name_def.name.lower():
                name_is_ok = False
        if name_is_ok:
            included_names[n] = name_def

    print(
        f"Removed {len(names.keys()) - len(included_names.keys())} hard to pronounce names containing {hard_to_pronounce}")
    return included_names


def exclude_hyphenated_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if '-' not in name_def.name:
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
            for meaning in name_def.get_all_meanings():
                if indicator in meaning.lower():
                    likely_an_alias = True
        if not likely_an_alias:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} meta-names")
    return included_names


def exclude_meaningless_names(names: Dict[str, NameDefinition]) -> Dict[str, NameDefinition]:
    included_names = {}
    for n in names:
        name_def = names[n]
        if len(name_def.get_all_meanings()) is not 0:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names with no meaning")
    return included_names


def exclude_israeli_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if Region.Israel not in name_def.get_all_origins():
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} Israeli names")
    return included_names


def exclude_muslim_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if Region.Muslim not in name_def.get_all_origins():
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} Muslim names")
    return included_names


def union_regions(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        origins = name_def.get_all_origins()
        likely_indian = any(o in indian_origins for o in origins)
        likely_western = any(o in western_origins for o in origins)
        if likely_indian or likely_western:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names which are neither Indian nor Western")
    return included_names


def intersect_regions(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        origins = name_def.get_all_origins()
        likely_indian = any(o in indian_origins for o in origins)
        likely_western = any(o in western_origins for o in origins)
        if likely_indian and likely_western:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names which are neither Indian nor Western")
    return included_names


def intersect_sources(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if NameSource.ssa in name_def.sources and NameSource.tamilcube in name_def.sources:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names which are neither Indian nor Western")
    return included_names


def exclude_short_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if len(name_def.name) > 3:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names that were shorter than four letters")
    return included_names


def exclude_religious_meanings(names: Dict[str, NameDefinition]):
    accepted_names = {}
    for n in names:
        name_def = names[n]
        likely_religious = False
        if name_def is None:
            continue
        for word in religious_indicators:
            if word in ','.join(name_def.get_all_meanings()).lower():
                likely_religious = True
        if not likely_religious:
            accepted_names[n] = names[n]
    print(f"Removed {len(names.keys()) - len(accepted_names.keys())} religious names")
    return accepted_names


def apply_filters(names_dict: Dict[str, NameDefinition]):
    filtered_names = names_dict
    filtered_names = exclude_hyphenated_names(filtered_names)
    filtered_names = exclude_names_ending_in(filtered_names)
    filtered_names = exclude_names_starting_in(filtered_names)
    filtered_names = exclude_hard_to_pronounce_names(filtered_names)
    filtered_names = exclude_nonlatin_names(filtered_names)
    filtered_names = exclude_meta_names(filtered_names)
    filtered_names = exclude_short_names(filtered_names)
    filtered_names = exclude_religious_meanings(filtered_names)
    filtered_names = exclude_boy_names(filtered_names)
    filtered_names = exclude_israeli_names(filtered_names)
    filtered_names = exclude_muslim_names(filtered_names)
    filtered_names = exclude_meaningless_names(filtered_names)
    # filtered_names = union_regions(filtered_names)
    # filtered_names = intersect_regions(filtered_names)
    # filtered_names = intersect_sources(filtered_names)
    print(f"filtered a total of {len(names_dict.keys()) - len(filtered_names.keys())} names")
    return filtered_names


def main():
    names_dict = read_names_json(names_json_filename)
    name_stats(names_dict)
    names_dict = apply_filters(names_dict)

    names_dataframe = name_dict_to_dataframe(names_dict)
    save_names_json(output_filename, names_dataframe)


if __name__ == "__main__":
    main()
