
import pytest

import calculator

def test_add():
    assert calculator.add(1, 2) == 3

def test_subs():
    assert calculator.subs(5, 2) == 3

def test_mult():
    assert calculator.mult(5, 2) == 10

def test_div():
    assert calculator.div(6, 2) == 3