#pytest discovery/test_first.py

def test_something(): # will run
    assert True
    
def not_a_test(): # will be ignored
    assert True


