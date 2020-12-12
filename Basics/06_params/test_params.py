import pytest

@pytest.fixture(params=[2,3,5])
def setup(request):
    retVal = request.param
    print("\nSetup! retval = {}".format(retVal))
    return retVal


def test1(setup):
    print("setup = {}".format(setup))
    assert True
