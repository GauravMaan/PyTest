import pytest
@pytest.fixture  # decorator-- annotation in testNG
def setup():
    print("Launch....")
    yield
    print("Closing")