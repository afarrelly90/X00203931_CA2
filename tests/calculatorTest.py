# tests for calculator app functions (3 per function)
import pytest
from app.calculator import add, sub, multi, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 0) == 0
    assert sub(-1, -1) == 0

def test_multi():
    assert multi(2, 3) == 6
    assert multi(-1, 1) == -1
    assert multi(0, 100) == 0

def test_div():
    assert div(6, 3) == 2
    assert div(-6, 2) == -3
    #divide by zero test
    with pytest.raises(ValueError):
        div(5, 0)