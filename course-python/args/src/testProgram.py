import pytest
from program import multiplication,is_eveen

print("hello world")

def test_multiplication():
    assert multiplication(1,2,3,4,5) == 120
    assert multiplication(1,2,3,4) == 24
    assert multiplication(0,1,2,3,4,5) == 0
    

def test_is_eveen():
    assert is_eveen(2) == "Eveen"
    assert is_eveen(3) == "Odd"
