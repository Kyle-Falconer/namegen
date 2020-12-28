import pytest
from Name import Gender


class TestGenderParse:
    def test_gender_boy(self):
        assert Gender.from_str('boy') is Gender.boy

    def test_gender_male(self):
        assert Gender.from_str('male') is Gender.boy

    def test_gender_m(self):
        assert Gender.from_str('m') is Gender.boy

    def test_gender_b(self):
        assert Gender.from_str('b') is Gender.boy

    def test_gender_girl(self):
        assert Gender.from_str('girl') is Gender.girl

    def test_gender_female(self):
        assert Gender.from_str('female') is Gender.girl

    def test_gender_f(self):
        assert Gender.from_str('f') is Gender.girl

    def test_gender_g(self):
        assert Gender.from_str('g') is Gender.girl

    def test_gender_either(self):
        assert Gender.from_str('either') is Gender.unisex

    def test_gender_morf(self):
        assert Gender.from_str('m or f') is Gender.unisex

    def test_gender_unisex(self):
        assert Gender.from_str('unisex') is Gender.unisex

    def test_gender_other(self):
        assert Gender.from_str('other') is Gender.unisex

    def test_gender_invalid(self):
        with pytest.raises(NotImplementedError):
            Gender.from_str('')
