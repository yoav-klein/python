
### This demonstrates that fixtures can be called more than once by the same test
### and return values are cached.

import pytest

# Arrange
@pytest.fixture
def second_entry():
    return "b"


# Arrange
@pytest.fixture
def order():
    return ["a"]

# Act
@pytest.fixture
def append_second(order, second_entry):
    return order.append(first_entry)

### You can see that the "order" object was cached. If not, "order" in this function
### would be a list with only "a" and the test would fail.
def test_string_only(append_second, order, second_entry):
    # Assert
    assert order == ["a", second_entry]