from Name import NameDefinition, Gender, Region, NameMeaning, NameSource
from names_filter import exclude_muslim_names, exclude_israeli_names, exclude_origins_only_in, exclude_non_palindromes, exclude_names_of_people_know


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
            NameMeaning("meaning1", [Region.Muslim]), NameMeaning("meaning2", [Region.United_States])])
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

    def test_exclude_origins_only_in_single(self):
        # assuming Spain appears in the exclude_only_origins list
        name1 = NameDefinition(name="name1", gender=Gender.girl, meanings=[NameMeaning("meaning1", [Region.Spain])])
        name2 = NameDefinition(name="name2", gender=Gender.girl, meanings=[NameMeaning("meaning1", [Region.India])])
        filtered = exclude_origins_only_in({
            "name1": name1,
            "name2": name2
        })
        assert len(filtered) is 1
        assert filtered == {"name2": name2}

    def test_exclude_origins_only_in_multiple(self):
        # assuming Spain and Latin_America both appear in the exclude_only_origins list
        name1 = NameDefinition(name="name1", gender=Gender.girl, meanings=[NameMeaning("meaning1", [
            Region.Spain, Region.Latin_America])])
        name2 = NameDefinition(name="name2", gender=Gender.girl, meanings=[NameMeaning("meaning1", [Region.India])])
        filtered = exclude_origins_only_in({
            "name1": name1,
            "name2": name2
        })
        assert len(filtered) is 1
        assert filtered == {"name2": name2}

    def test_exclude_origins_only_in_multiple_exception(self):
        # assuming Spain and Latin_America both appear in the exclude_only_origins list
        name1 = NameDefinition(name="name1", gender=Gender.girl, meanings=[NameMeaning("meaning1", [
            Region.Spain, Region.Latin_America, Region.United_States])])
        name2 = NameDefinition(name="name2", gender=Gender.girl, meanings=[NameMeaning("meaning1", [Region.India])])
        filtered = exclude_origins_only_in({
            "name1": name1,
            "name2": name2
        })
        assert len(filtered) is 2
        assert filtered == {"name1": name1, "name2": name2}

    def test_palindromes(self):
        # test where the meaning only has the excluded meaning
        name1 = NameDefinition(name="name1eman", gender=Gender.girl,
                               meanings=[NameMeaning("meaning1", [Region.Muslim])])
        name2 = NameDefinition(name="name2", gender=Gender.girl, meanings=[NameMeaning("meaning1", [Region.India])])
        filtered = exclude_non_palindromes({
            "name1eman": name1,
            "name2": name2
        })
        assert len(filtered) is 1
        assert filtered == {"name1eman": name1}

    def test_similar_name_exclude(self):
        name1 = NameDefinition(name="Ailin", gender=Gender.boy, source=NameSource.people_we_know)
        name2 = NameDefinition(name="Aaelin", gender=Gender.boy, source=NameSource.ssa)
        name3 = NameDefinition(name="Josh", gender=Gender.boy, source=NameSource.ssa)
        filtered = exclude_names_of_people_know({
            "Ailin": name1,
            "Aaelin": name2,
            'Josh': name3
        }, filter_metaphones=True)
        assert len(filtered) is 1
        assert filtered == {'Josh': name3}
