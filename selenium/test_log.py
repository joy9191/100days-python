import pytest


class TestCase(object):
    def test_eq_set(self):
        assert {0, 10, 11, 12} == {0, 20, 21}

    def test_eq_dict(self):
        assert {'a': 0, 'b': 1, 'c': 0} == {'a': 0, 'b': 2, 'd': 0}

    def test_eq_list(self):
        assert [0, 1, 2] == [0, 1, 3]

    def test_eq_longer_list(self):
        assert [1, 2] == [1, 2, 3]