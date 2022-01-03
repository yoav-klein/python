
### Demonstrates module scoped fixture.
###     Note that if the order() fixture is module scoped (in the conftest)
###     the test_string_and_int test fails, since one "a" is already appended to it
###     
###     but if we put it here, function-scoped, each call to order() will get a fresh empty list
###     thus will succeed

import pytest

# @pytest.fixture
# def order():
#     return []

@pytest.fixture(autouse=True)
def append_first(order):
    return order.append("a")


def test_string_only(order):
    assert order == ["a"]


def test_string_and_int(order):
    order.append(2)
    assert order == ["a", 2]