import pytest

class TestClass:
    @pytest.mark.skip
    def test_Method1(self,setup):
        print("hello")
    def test_Method2(self,setup):
        print("bro")