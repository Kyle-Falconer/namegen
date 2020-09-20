import os, csv

from typing import List

from Name import NameDefinition, Gender, Region

from file_utils import save_names, name_list_to_dataframe

# input lists
pantheon_filename = os.path.join("name_lists", "pantheon.tsv")
ssa_names_filename = os.path.join("name_lists", "ssa-baby-names.csv")
indian_names_filename = os.path.join("name_lists", "tamilcube_scraped_names.csv")
star_trek_filename = os.path.join("name_lists", "star_trek.csv")
meaning_of_names_filename = os.path.join("name_lists", "meaning_of_names_scraped_names.csv")

# output list
merged_output_filename = os.path.join("name_lists", "names_merged.csv")


def intake_indian_names() -> List[NameDefinition]:
    print(f"reading names from {indian_names_filename}")
    number_merged = 0
    number_added = 0
    names = {}
    with open(indian_names_filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if row['Name'] in names and names[row['Name']] is not None:
                existing_name = names[row['Name']]
                existing_name.append_attrs(gender=Gender.from_str(row['Gender']),
                                           meaning=row['Meaning'],
                                           origin=Region.from_str(row['Language']))
                names[row['Name']] = existing_name
                number_merged = number_merged + 1
            else:
                names[row['Name']] = NameDefinition(name=row['Name'],
                                                    gender=Gender.from_str(row['Gender']),
                                                    meaning=row['Meaning'],
                                                    origin=Region.from_str(row['Language']))
                number_added = number_added + 1

    print(f"added {number_added} and merged/updated {number_merged} Indian name definitions")
    return list(names.values())


def intake_ssa_names() -> List[NameDefinition]:
    print(f"reading names from {ssa_names_filename}")
    number_merged = 0
    number_added = 0
    names = {}
    with open(ssa_names_filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if row['name'] in names and names[row['name']] is not None:
                existing_name = names[row['name']]
                existing_name.append_attrs(gender=Gender.from_str(row['sex']))
                names[row['name']] = existing_name
                number_merged = number_merged + 1
            else:
                names[row['name']] = NameDefinition(name=row['name'],
                                                    gender=Gender.from_str(row['sex']))
                number_added = number_added + 1

    print(f"added {number_added} and merged/updated {number_merged} name definitions from the SSA")
    return list(names.values())


def intake_mon_names() -> List[NameDefinition]:
    print(f"reading names from {meaning_of_names_filename}")
    number_merged = 0
    number_added = 0
    names = {}
    with open(meaning_of_names_filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if row['name'] in names and names[row['name']] is not None:
                existing_name = names[row['name']]
                existing_name.append_attrs(gender=Gender.from_str(row['gender']),
                                           origin=Region.from_str(row['origin']),
                                           meaning=row['meaning'])
                names[row['name']] = existing_name
                number_merged = number_merged + 1
            else:
                names[row['name']] = NameDefinition(name=row['name'],
                                                    gender=Gender.from_str(row['gender']),
                                                    origin=Region.from_str(row['origin']),
                                                    meaning=row['meaning'])
                number_added = number_added + 1

    print(f"added {number_added} and merged/updated {number_merged} name definitions from the meaning-of-names.com")
    return list(names.values())


def intake_star_trek() -> List[NameDefinition]:
    print(f"reading names from {star_trek_filename}")
    number_merged = 0
    number_added = 0
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
            first_name=f"{row['First Name']}"
            character_name=f"{rank}{row['Character']} from Star Trek"
            if first_name in names and names[first_name] is not None:
                existing_name = names[first_name]
                existing_name.append_attrs(gender=Gender.from_str(row['Gender']),
                                           known_persons = character_name)
                names[first_name] = existing_name
                number_merged = number_merged + 1
            else:
                names[first_name] =  NameDefinition(name=first_name,
                                              gender=Gender.from_str(row['Gender']),
                                              known_persons=character_name)
                number_added = number_added + 1

    print(f"added {number_added} and merged/updated {number_merged} name definitions from Star Trek")
    return list(names.values())


def intake_pantheon() -> List[NameDefinition]:
    print(f"reading names from {pantheon_filename}")
    names = {}
    number_merged = 0
    number_added = 0
    with open(pantheon_filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter='\t', quotechar='"')
        for row in csvreader:
            person_fname = row['name'].split(' ')[0]
            famous_person = f"{row['occupation'].title()} {row['name']}"
            if person_fname in names and names[person_fname] is not None:
                existing_name = names[person_fname]
                existing_name.append_attrs(gender=Gender.from_str(row['gender']),
                                           origin=Region.from_str(row['countryName']),
                                           known_persons=famous_person)
                names[person_fname] = existing_name
                number_merged = number_merged + 1
            else:
                names[person_fname] = NameDefinition(name=person_fname,
                                                     gender=Gender.from_str(row['gender']),
                                                     origin=Region.from_str(row['countryName']),
                                                     known_persons=famous_person)
                number_added = number_added + 1
    print(f"added {number_added} and merged/updated {number_merged} name definitions from the pantheon")
    return list(names.values())


def sort_merged(mixed_names: List[NameDefinition]) -> List[NameDefinition]:
    sorted_names = {}
    number_merged = 0
    number_added = 0
    for n in mixed_names:
        if n.name in sorted_names and sorted_names[n.name] is not None:
            existing_name = sorted_names.get(n.name)
            existing_name.merge_name(n)
            sorted_names[n.name] = existing_name
            number_merged = number_merged + 1
        else:
            sorted_names[n.name] = n
            number_added = number_added + 1
    print(f"sorted a total of {len(sorted_names.keys())} and merged/updated {number_merged} names")
    return sorted(list(sorted_names.values()), key=lambda x: x.name)


def main():
    all_names = []
    all_names = all_names + intake_mon_names()
    all_names = all_names + intake_indian_names()
    all_names = all_names + intake_pantheon()
    all_names = all_names + intake_ssa_names()
    all_names = all_names + intake_star_trek()

    all_names = sort_merged(all_names)

    names_df = name_list_to_dataframe(all_names)
    save_names(merged_output_filename, names_df)


if __name__ == "__main__":
    main()
