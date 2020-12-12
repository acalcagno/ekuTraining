import pytest

@pytest.fixture(scope="module", autouse=True)
def setupModule2():
    print("\nSetup Module2")


@pytest.fixture(scope="class", autouse=True)
def setupClass():
    print("\nSetup class")


@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function")


class TestClass:
    def test1(self):
        print("TestIt")
        assert True

    def test2(self):
        print("TestIt2!")
        assert True
