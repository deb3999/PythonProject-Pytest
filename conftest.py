import pytest
@pytest.fixture
def setup():
    print("browser is launched")
    yield
    print("browser closed")