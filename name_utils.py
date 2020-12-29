from typing import Dict

from Name import NameDefinition
from name_constants import indian_origins, western_origins


def name_stats(names_dict: Dict[str, NameDefinition]):
    english_count = 0
    indian_count = 0
    multisource_names_count = 0
    for name in names_dict:
        origins = names_dict[name].get_all_origins()
        likely_indian = any(o in indian_origins for o in origins)
        likely_english = any(o in western_origins for o in origins)
        if likely_indian:
            indian_count = indian_count + 1
        if likely_english:
            english_count = english_count + 1
        if len(names_dict[name].sources) > 1:
            multisource_names_count = multisource_names_count + 1
    print(f"Counted {indian_count} Indian names and {english_count} English names")
    print(f"{multisource_names_count} names are mentioned in more than one source")

