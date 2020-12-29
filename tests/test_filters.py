from Name import NameDefinition, Gender, Region, NameMeaning
from names_filter import exclude_muslim_names, exclude_israeli_names


class TestFilters:
    def test_exclude_muslim_pure_filter(self):
        # test where the meaning only has the excluded meaning
        name1 = NameDefinition(name="name1", gender=Gender.girl, meanings=[NameMeaning("meaning1", [Region.Muslim])])
        name2 = NameDefinition(name="name2", gender=Gender.girl, meanings=[NameMeaning("meaning1", [Region.India])])
        filtered = exclude_muslim_names({
            "name1": name1,
            "name2": name2
        })
        assert len(filtered) is 1
        assert filtered == {"name2": name2}

    def test_exclude_muslim_mixed_filter(self):
        # test where the meaning contains the excluded meaning
        name1 = NameDefinition(name="name1", gender=Gender.girl, meanings=[
            NameMeaning("meaning1", [Region.Muslim]),  NameMeaning("meaning2", [Region.United_States])])
        name2 = NameDefinition(name="name2", gender=Gender.girl, meanings=[NameMeaning("meaning1", [Region.India])])
        filtered = exclude_muslim_names({
            "name1": name1,
            "name2": name2
        })
        assert len(filtered) is 1
        assert filtered == {"name2": name2}

    def test_exclude_israeli_pure_filter(self):
        # test where the meaning only has the excluded meaning
        name1 = NameDefinition(name="name1", gender=Gender.girl, meanings=[NameMeaning("meaning1", [Region.Israel])])
        name2 = NameDefinition(name="name2", gender=Gender.girl, meanings=[NameMeaning("meaning1", [Region.India])])
        filtered = exclude_israeli_names({
            "name1": name1,
            "name2": name2
        })
        assert len(filtered) is 1
        assert filtered == {"name2": name2}

    def test_exclude_israeli_mixed_filter(self):
        # test where the meaning contains the excluded meaning
        name1 = NameDefinition(name="name1", gender=Gender.girl, meanings=[
            NameMeaning("meaning1", [Region.Israel]), NameMeaning("meaning2", [Region.United_States])])
        name2 = NameDefinition(name="name2", gender=Gender.girl, meanings=[NameMeaning("meaning1", [Region.India])])
        filtered = exclude_israeli_names({
            "name1": name1,
            "name2": name2
        })
        assert len(filtered) is 1
        assert filtered == {"name2": name2}