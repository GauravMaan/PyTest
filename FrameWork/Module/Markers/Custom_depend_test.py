import pytest


class TestClass:
    @pytest.mark.dependency
    def test_openApp(self):
        assert True

    @pytest.mark.dependency(depends=["test_openApp"])
    def test_Method1(self):
        assert True

    @pytest.mark.dependency(depends=["test_openApp"])
    def test_Method2(self):
        print("bro")