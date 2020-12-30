import os, csv, json

from typing import List, Dict

from Name import NameDefinition, Gender, Region, NameSource

from file_utils import save_names_csv, save_names_json, name_list_to_dataframe

# input lists
from name_utils import name_stats

pantheon_filename = os.path.join("name_lists", "pantheon.tsv")
ssa_names_filename = os.path.join("name_lists", "ssa-baby-names.csv")
indian_names_filename = os.path.join("name_lists", "tamilcube_scraped_names.csv")
star_trek_filename = os.path.join("name_lists", "star_trek.csv")
meaning_of_names_filename = os.path.join("name_lists", "meaning_of_names_scraped_names.csv")
strippers_filename = os.path.join("name_lists", "stripper_names.txt")
people_we_know_filename = os.path.join("name_lists", "people_we_know.txt")

# output list
merged_output_csv_filename = os.path.join("name_lists", "names_merged.csv")
merged_output_json_filename = os.path.join("name_lists", "names_merged.json")


def intake_indian_names(names: Dict[str, NameDefinition] = None) -> Dict[str, NameDefinition]:
    print(f"reading names from {indian_names_filename}")
    number_merged = 0
    number_added = 0
    if names is None:
        names = {}
    with open(indian_names_filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if row['Name'] in names and names[row['Name']] is not None:
                existing_name = names[row['Name']]
                existing_name.append_attrs(gender=Gender.from_str(row['Gender']),
                                           meaning=row['Meaning'],
                                           origin=Region.from_str(row['Language']),
                                           source=NameSource.tamilcube)
                names[row['Name']] = existing_name
                number_merged = number_merged + 1
            else:
                names[row['Name']] = NameDefinition(name=row['Name'],
                                                    gender=Gender.from_str(row['Gender']),
                                                    meaning=row['Meaning'],
                                                    origin=Region.from_str(row['Language']),
                                                    source=NameSource.tamilcube)
                number_added = number_added + 1

    print(f"added {number_added} and merged/updated {number_merged} Indian name definitions")
    return names


def intake_ssa_names(names: Dict[str, NameDefinition] = None) -> Dict[str, NameDefinition]:
    print(f"reading names from {ssa_names_filename}")
    number_merged = 0
    number_added = 0
    if names is None:
        names = {}
    with open(ssa_names_filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if row['name'] in names and names[row['name']] is not None:
                existing_name = names[row['name']]
                existing_name.append_attrs(gender=Gender.from_str(row['sex']), source=NameSource.ssa)
                names[row['name']] = existing_name
                number_merged = number_merged + 1
            else:
                names[row['name']] = NameDefinition(name=row['name'],
                                                    gender=Gender.from_str(row['sex']),
                                                    source=NameSource.ssa)
                number_added = number_added + 1

    print(f"added {number_added} and merged/updated {number_merged} name definitions from the SSA")
    return names


def intake_mon_names(names: Dict[str, NameDefinition] = None) -> Dict[str, NameDefinition]:
    print(f"reading names from {meaning_of_names_filename}")
    number_merged = 0
    number_added = 0
    if names is None:
        names = {}
    with open(meaning_of_names_filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if row['name'] in names and names[row['name']] is not None:
                existing_name = names[row['name']]
                existing_name.append_attrs(gender=Gender.from_str(row['gender']),
                                           origin=Region.from_str(row['origin']),
                                           meaning=row['meaning'],
                                           source=NameSource.meaning_of_names)
                names[row['name']] = existing_name
                number_merged = number_merged + 1
            else:
                names[row['name']] = NameDefinition(name=row['name'],
                                                    gender=Gender.from_str(row['gender']),
                                                    origin=Region.from_str(row['origin']),
                                                    meaning=row['meaning'],
                                                    source=NameSource.meaning_of_names)
                number_added = number_added + 1

    print(f"added {number_added} and merged/updated {number_merged} name definitions from the meaning-of-names.com")
    return names


def intake_star_trek(names: Dict[str, NameDefinition] = None) -> Dict[str, NameDefinition]:
    print(f"reading names from {star_trek_filename}")
    number_merged = 0
    number_added = 0
    if names is None:
        names = {}
    with open(star_trek_filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if len(row['First Name'].strip()) is 0:
                continue
            rank = ''
            if row['Rank'] and row['Rank'].lower() != "civilian":
                rank = row['Rank'].split(',')[0].strip()
                if len(rank) is not 0:
                    rank = f"{rank} "
            first_name = f"{row['First Name']}"
            character_name = f"{rank}{row['Character']} from Star Trek"
            if first_name in names and names[first_name] is not None:
                existing_name = names[first_name]
                existing_name.append_attrs(gender=Gender.from_str(row['Gender']),
                                           known_persons=character_name,
                                           source=NameSource.star_trek)
                names[first_name] = existing_name
                number_merged = number_merged + 1
            else:
                names[first_name] = NameDefinition(name=first_name,
                                                   gender=Gender.from_str(row['Gender']),
                                                   known_persons=character_name,
                                                   source=NameSource.star_trek)
                number_added = number_added + 1

    print(f"added {number_added} and merged/updated {number_merged} name definitions from Star Trek")
    return names


def intake_pantheon(names: Dict[str, NameDefinition] = None) -> Dict[str, NameDefinition]:
    print(f"reading names from {pantheon_filename}")
    number_merged = 0
    number_added = 0
    if names is None:
        names = {}
    with open(pantheon_filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter='\t', quotechar='"')
        for row in csvreader:
            person_fname = row['name'].split(' ')[0]
            famous_person = f"{row['occupation'].title()} {row['name']}"
            if person_fname in names and names[person_fname] is not None:
                existing_name = names[person_fname]
                existing_name.append_attrs(gender=Gender.from_str(row['gender']),
                                           origin=Region.from_str(row['countryName']),
                                           known_persons=famous_person,
                                           source=NameSource.pantheon)
                names[person_fname] = existing_name
                number_merged = number_merged + 1
            else:
                names[person_fname] = NameDefinition(name=person_fname,
                                                     gender=Gender.from_str(row['gender']),
                                                     origin=Region.from_str(row['countryName']),
                                                     known_persons=famous_person,
                                                     source=NameSource.pantheon)
                number_added = number_added + 1
    print(f"added {number_added} and merged/updated {number_merged} name definitions from the pantheon")
    return names


def intake_strippers(names: Dict[str, NameDefinition] = None) -> Dict[str, NameDefinition]:
    print(f"reading names from {strippers_filename}")
    number_merged = 0
    number_added = 0
    if names is None:
        names = {}
    with open(strippers_filename) as file:
        content = file.readlines()
        for line in content:
            name = line.strip()
            if name in names and names[name] is not None:
                existing_name = names[name]
                existing_name.append_attrs(source=NameSource.stripper)
                names[name] = existing_name
                number_merged = number_merged + 1
            else:
                names[name] = NameDefinition(name=name, source=NameSource.stripper)
                number_added = number_added + 1
    print(f"added {number_added} and merged/updated {number_merged} name definitions from the stripper name list")
    return names


def intake_people_we_know(names: Dict[str, NameDefinition] = None) -> Dict[str, NameDefinition]:
    print(f"reading names from {people_we_know_filename}")
    number_merged = 0
    number_added = 0
    if names is None:
        names = {}
    with open(people_we_know_filename) as file:
        content = file.readlines()
        for line in content:
            name = line.strip()
            if name in names and names[name] is not None:
                existing_name = names[name]
                existing_name.append_attrs(source=NameSource.people_we_know)
                names[name] = existing_name
                number_merged = number_merged + 1
            else:
                names[name] = NameDefinition(name=name, source=NameSource.people_we_know)
                number_added = number_added + 1
    print(f"added {number_added} and merged/updated {number_merged} name definitions from the people we know name list")
    return names


def main():
    all_names = {}
    all_names = intake_mon_names(all_names)
    all_names = intake_indian_names(all_names)
    all_names = intake_pantheon(all_names)
    all_names = intake_ssa_names(all_names)
    all_names = intake_star_trek(all_names)
    all_names = intake_strippers(all_names)
    all_names = intake_people_we_know(all_names)

    name_stats(all_names)

    sorted_names = sorted(list(all_names.values()), key=lambda x: x.name)
    names_df = name_list_to_dataframe(sorted_names)
    # save_names_csv(merged_output_csv_filename, names_df)
    save_names_json(merged_output_json_filename, names_df)


if __name__ == "__main__":
    main()
