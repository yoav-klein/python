###########################################
#       
#   Demonstration of class-scoped fixture
#
#   In this example, you can see the inc() fixture
#   which increments the value of foo._count
#
#   Since the fixture is scoped to the class, it only
#   runs once for all the tests in the class. 
#   If you remove the (scope="class") from the decorator
#   one of the tests will fail.
#
##############################################



import pytest

class Foo:
    def __init__(self):
        self._count = 0
    
    def increment(self):
        self._count += 1

foo = Foo()

class TestFoo:
    @pytest.fixture(scope="class")
    def inc(self):
        foo.increment()
        return foo._count

    def test_one(self, inc):
        assert inc == 1
    
    def test_two(self, inc):
        assert inc == 1
