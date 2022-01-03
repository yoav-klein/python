
## This example demonstrates asserting that a certain exception has been raised

import pytest

def f():
    raise ValueError("some error")
    
def test_raise():
    with pytest.raises(ValueError):
        f()
