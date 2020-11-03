def setup_module(module):
    print("setup module")

def teardown_module(module):
    print("tearing down module module")



def setup_function(function):
    if function == test1:
        print("\nSetting up test1")
    elif function == test2:
        print("\nSetting up test2")
    else:
        print("\nSetting up unknown test")

def teardown_function(function):
    if function == test1:
        print("\nTearing donw test1")
    elif function == test1:
        print("\nTearing donw test2")
    else:
        print("\nTearing donw unknown test")

def test1():
    print("executing test 1")
    assert True

def test2():
    print("executing test 2")
    assert True
