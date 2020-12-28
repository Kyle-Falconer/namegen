import pytest
import json

from Name import NameDefinition, Gender, Region


class TestNames:
    def test_meaning_none(self):
        name = NameDefinition(name="name1", gender=Gender.boy, meaning=None)
        assert len(name.meanings) is 0

    def test_meaning_merge_same_origin(self):
        name = NameDefinition(name="name1", gender=Gender.boy, meaning="meaning1", origin=Region.United_States)
        name.add_meaning(meaning="meaning2", origin=Region.United_States)
        assert len(name.meanings) is 2
        assert name.meanings[0].meaning == "meaning1"
        assert name.meanings[0].origins == [Region.United_States]
        assert name.meanings[1].meaning == "meaning2"
        assert name.meanings[1].origins == [Region.United_States]

    def test_meaning_merge_same_meaning_different_origins(self):
        name = NameDefinition(name="name1", gender=Gender.boy, meaning="meaning1", origin=Region.United_States)
        name.add_meaning(meaning="meaning1", origin=Region.United_Kingdom)
        assert len(name.meanings) is 1
        assert name.meanings[0].meaning == "meaning1"
        assert name.meanings[0].origins == [Region.United_States, Region.United_Kingdom]

    def test_gender_boy_to_unisex(self):
        name = NameDefinition(name="name1", gender=Gender.boy)
        assert name.gender == Gender.boy
        name.append_attrs(gender=Gender.girl)
        assert name.gender == Gender.unisex

    def test_gender_girl_to_unisex(self):
        name = NameDefinition(name="name1", gender=Gender.girl)
        assert name.gender == Gender.girl
        name.append_attrs(gender=Gender.boy)
        assert name.gender == Gender.unisex

    def test_gender_unisex_to_girl_still_unisex(self):
        name = NameDefinition(name="name1", gender=Gender.unisex)
        assert name.gender == Gender.unisex
        name.append_attrs(gender=Gender.girl)
        assert name.gender == Gender.unisex

    def test_gender_unisex_to_boy_still_unisex(self):
        name = NameDefinition(name="name1", gender=Gender.unisex)
        assert name.gender == Gender.unisex
        name.append_attrs(gender=Gender.boy)
        assert name.gender == Gender.unisex

    def test_name_to_dict(self):
        name = NameDefinition(name="name1", gender=Gender.boy, meaning="meaning1", origin=Region.United_States)
        name_dict = name.to_dict()
        name_json = json.dumps(name_dict)
        assert name_json == '{"name": "name1", "gender": "boy", "meaning": [{"meaning": "meaning1", "origins": ["United States"]}], "known_persons": ""}'

    def test_get_all_origins_same_meaning(self):
        name = NameDefinition(name="name1", gender=Gender.boy, meaning="meaning1", origin=Region.United_States)
        name.add_meaning("meaning1", origin=Region.United_Kingdom)
        assert name.get_all_origins() == [Region.United_States, Region.United_Kingdom].sort()

    def test_get_all_origins_different_meanings(self):
        name = NameDefinition(name="name1", gender=Gender.boy, meaning="meaning1", origin=Region.United_States)
        name.add_meaning("meaning1", origin=Region.United_Kingdom)
        name.add_meaning("meaning2", origin=Region.India)
        name.add_meaning("meaning2", origin=Region.Tamil)
        assert name.get_all_origins() == [Region.United_Kingdom, Region.United_States, Region.India, Region.Tamil].sort()

    def test_get_all_meanings_same_meaning(self):
        name = NameDefinition(name="name1", gender=Gender.boy, meaning="meaning1", origin=Region.United_States)
        name.add_meaning("meaning1", origin=Region.United_Kingdom)
        assert name.get_all_meanings() == ["meaning1"]

    def test_get_all_meanings_different_meanings(self):
        name = NameDefinition(name="name1", gender=Gender.boy, meaning="meaning1", origin=Region.United_States)
        name.add_meaning("meaning1", origin=Region.United_Kingdom)
        name.add_meaning("meaning2", origin=Region.India)
        name.add_meaning("meaning2", origin=Region.Tamil)
        assert name.get_all_meanings() == ["meaning1", "meaning2"]