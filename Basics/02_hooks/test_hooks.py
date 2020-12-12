def setup_module(module):
    print("setup module")

def teardown_module(module):
    print("tearing down module {}".format(module.__name__))

def setup_function(function):
    print("\nSetting up function {}".format(function.__name__))

def teardown_function(function):
    print("\Tearing down function {}".format(function.__name__))    

def test1():
    print("executing test 1")
    assert True

def test2():
    print("executing test 2")
    assert True
