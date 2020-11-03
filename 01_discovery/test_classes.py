#pytest discovery/test_classes.py


class TestClass: # will be run
	def test_me(self): 
		assert True

	def test_me2(self): # will be run
		assert True

class MyTestClass: # will be ignored
	def test_it(self): 
		assert True

	def test_it2(self): 
		assert True
