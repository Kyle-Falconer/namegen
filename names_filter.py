import os
import re
from string import ascii_letters
from typing import Dict

from Name import NameDefinition, Gender, Region, NameSource
from file_utils import read_names_json, name_dict_to_dataframe, save_names_json
from name_constants import excluded_name_endings, hard_to_pronounce, excluded_startings, western_origins, \
    indian_origins, \
    religious_indicators, excluded_contains, exclude_only_origins
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
        if not name_def.name.lower().endswith(excluded_name_endings):
            included_names[n] = name_def

    print(f"Removed {len(names.keys()) - len(included_names.keys())} names ending in {excluded_name_endings}")
    return included_names


def exclude_names_containing_excluded(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        contains_excluded = False
        for snippet in excluded_contains:
            if snippet in name_def.name:
                contains_excluded = True
        if not contains_excluded:
            included_names[n] = name_def

    print(f"Removed {len(names.keys()) - len(included_names.keys())} names containing: {excluded_contains}")
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


def exclude_girl_names(names: Dict[str, NameDefinition]) -> Dict[str, NameDefinition]:
    included_names = {}
    for n in names:
        name_def = names[n]
        if name_def.gender != Gender.girl:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} girl names")
    return included_names


def exclude_unisex_names(names: Dict[str, NameDefinition]) -> Dict[str, NameDefinition]:
    included_names = {}
    for n in names:
        name_def = names[n]
        if name_def.gender != Gender.unisex:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} unisex names")
    return included_names


def exclude_meta_names(names: Dict[str, NameDefinition]) -> Dict[str, NameDefinition]:
    alias_indicators = ['variant of ', 'variation of ', 'diminutive of ', 'abbreviation of ', 'derived from ',
                        'surname']
    included_names = {}
    for n in names:
        likely_an_alias = False
        name_def = names[n]
        collected_meaning = ','.join(name_def.get_all_meanings()).lower()
        for indicator in alias_indicators:
            if indicator in collected_meaning:
                likely_an_alias = True
        if not likely_an_alias:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} meta-names")
    return included_names


def exclude_date_names(names: Dict[str, NameDefinition]) -> Dict[str, NameDefinition]:
    date_indicators = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'january',
                       'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                       'november', 'december', 'spring', 'summer', 'fall', 'winter']
    included_names = {}
    for n in names:
        likely_a_date_name = False
        name_def = names[n]
        collected_meaning = ','.join(name_def.get_all_meanings()).lower()
        for indicator in date_indicators:
            if indicator in collected_meaning or indicator in name_def.name.lower():
                likely_a_date_name = True
        if not likely_a_date_name:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} date-based names")
    return included_names


def exclude_birth_order_names(names: Dict[str, NameDefinition]) -> Dict[str, NameDefinition]:
    date_indicators = ['born']
    included_names = {}
    for n in names:
        likely_an_alias = False
        name_def = names[n]
        collected_meaning = ','.join(name_def.get_all_meanings()).lower()
        for indicator in date_indicators:
            if indicator in collected_meaning:
                likely_an_alias = True
        if not likely_an_alias:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} birth-order names")
    return included_names


def exclude_meaningless_names(names: Dict[str, NameDefinition]) -> Dict[str, NameDefinition]:
    included_names = {}
    for n in names:
        name_def = names[n]
        if len(name_def.get_all_meanings()) is not 0:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names with no meaning")
    return included_names


def exclude_non_ssa_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if NameSource.ssa in name_def.sources:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names that were not in the SSA dataset")
    return included_names


def exclude_us_state_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if NameSource.us_states not in name_def.sources:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names that are the same as U.S. State names")
    return included_names


def exclude_country_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if NameSource.countries not in name_def.sources:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names that are the same as country names")
    return included_names

def exclude_stripper_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if NameSource.stripper not in name_def.sources:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} stripper names")
    return included_names


def exclude_names_of_people_know(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if NameSource.people_we_know not in name_def.sources:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names of people we know")
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


def exclude_origins_only_in(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        name_origins = name_def.get_all_origins()
        name_origins = list(filter(lambda i: i not in exclude_only_origins, name_origins))
        if len(name_origins) > 0:
            included_names[n] = name_def

    print(f"Removed {len(names.keys()) - len(included_names.keys())} single origin names from the excluded regions")
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


def exclude_combination_names(names: Dict[str, NameDefinition]):
    included_names = {}
    for n in names:
        name_def = names[n]
        if len(re.findall(r'[A-Z]', name_def.name)) < 2:
            included_names[n] = name_def
    print(f"Removed {len(names.keys()) - len(included_names.keys())} names containing more than one capital letter")
    return included_names


def exclude_religious_meanings(names: Dict[str, NameDefinition]):
    accepted_names = {}
    for n in names:
        name_def = names[n]
        likely_religious = False
        if name_def is None:
            continue
        collected_meaning = ','.join(name_def.get_all_meanings()).lower()
        for word in religious_indicators:
            if word in collected_meaning:
                likely_religious = True
        if not likely_religious:
            accepted_names[n] = names[n]
    print(f"Removed {len(names.keys()) - len(accepted_names.keys())} religious names")
    return accepted_names


def apply_filters(names_dict: Dict[str, NameDefinition]):
    filtered_names = names_dict

    # character-based exclusions
    filtered_names = exclude_hyphenated_names(filtered_names)
    filtered_names = exclude_nonlatin_names(filtered_names)
    filtered_names = exclude_short_names(filtered_names)
    filtered_names = exclude_combination_names(filtered_names)
    filtered_names = exclude_names_ending_in(filtered_names)
    filtered_names = exclude_names_containing_excluded(filtered_names)
    filtered_names = exclude_names_starting_in(filtered_names)
    filtered_names = exclude_hard_to_pronounce_names(filtered_names)
    print(f"{len(filtered_names)} names remain after character-based exclusions")

    # uncomment one or two of these, depending on desired gender
    filtered_names = exclude_boy_names(filtered_names)
    # filtered_names = exclude_girl_names(filtered_names)
    # filtered_names = exclude_unisex_names(filtered_names)
    print(f"{len(filtered_names)} names remain after gender-based exclusions")

    # meaning-based exclusions
    filtered_names = exclude_meaningless_names(filtered_names)
    filtered_names = exclude_meta_names(filtered_names)
    filtered_names = exclude_date_names(filtered_names)
    filtered_names = exclude_us_state_names(filtered_names)
    filtered_names = exclude_country_names(filtered_names)
    filtered_names = exclude_birth_order_names(filtered_names)
    filtered_names = exclude_religious_meanings(filtered_names)
    print(f"{len(filtered_names)} names remain after meaning-based exclusions")

    # region or origin exclusions
    # filtered_names = exclude_non_ssa_names(filtered_names)
    filtered_names = exclude_stripper_names(filtered_names)
    filtered_names = exclude_names_of_people_know(filtered_names)
    filtered_names = exclude_origins_only_in(filtered_names)
    filtered_names = exclude_israeli_names(filtered_names)
    filtered_names = exclude_muslim_names(filtered_names)
    # filtered_names = union_regions(filtered_names)
    # filtered_names = intersect_regions(filtered_names)
    # filtered_names = intersect_sources(filtered_names)
    print(f"{len(filtered_names)} names remain after region and origin exclusions")

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
