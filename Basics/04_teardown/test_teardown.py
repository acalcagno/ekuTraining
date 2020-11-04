import pytest

@pytest.fixture()
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")

@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teardonw_a():
        print("\nTearing down A")

    def teardonw_b():
        print("\nTearing down B")

    request.addfinalizer(teardonw_a)
    request.addfinalizer(teardonw_b)

def test1(setup1):
    print("\nExecuting Test 1")
    assert True

def test2(setup2):
    print("\nExecuting Test 2")
    assert True    