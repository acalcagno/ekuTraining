class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup {}".format(cls.__name__))

    @classmethod
    def teardown_class(cls):
        print("Teardown {}".format(cls.__name__))

    def setup_method(self, method):
        print("\nSetting up method{}".format(method.__name__))

    def teardown_method(self, method):
        print("\nTearing down method {}".format(method.__name__))

    def test1(self):
        print('Executing test1!')
        assert True

    def test2(self):
        print('Executing test2!')
        assert True
        