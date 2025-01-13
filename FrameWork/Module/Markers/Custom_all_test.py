import pytest

class TestExample:

    @pytest.mark.first
    @pytest.mark.order(1)
    def test_alpha(self):
        assert True

    @pytest.mark.second
    @pytest.mark.order(2)
    def test_gamma(self):
        assert False

    @pytest.mark.third
    @pytest.mark.order(3)
    def test_beta(self):
        assert True