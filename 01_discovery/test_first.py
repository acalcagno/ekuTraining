#pytest discovery/test_first.py

def test_something(): # will be run
    assert True
    
def not_a_test(): # will be ignored
    assert True


