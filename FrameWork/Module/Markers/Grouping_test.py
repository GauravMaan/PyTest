import pytest

class TestExample:

    @pytest.mark.sanity
    def test_alpha(self):
        assert True

    @pytest.mark.regression
    def test_gamma(self):
        assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_beta(self):
        assert True