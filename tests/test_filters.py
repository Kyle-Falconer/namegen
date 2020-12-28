import json

from Name import NameDefinition, Gender, Region, NameMeaning
from names_filter import exclude_muslim_names


class TestFilters:
    def test_remove_muslim_filter(self):
        name1 = NameDefinition(name="Aamanee", gender=Gender.girl, meanings=[NameMeaning("good wish", [Region.Muslim])])
        name2 = NameDefinition(name="Aashka", gender=Gender.girl, meanings=[NameMeaning("blessing", [Region.India])])
        filtered = exclude_muslim_names({
            "Aamanee": name1,
            "Aashka": name2
        })
        assert len(filtered) is 1
        assert filtered == {"Aashka": name2}
