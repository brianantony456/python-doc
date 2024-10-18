# tests/module1/test_submodule1.py
import pytest
from reader_doc.module1.submodule1 import Submodule1

@pytest.fixture
def submodule():
    return Submodule1()

def test_do_something(submodule):
    result = submodule.do_something()
    assert result == "Submodule1 is doing something"

def test_do_something_with_submodule2(submodule):
    result = submodule.do_something_with_submodule2()
    assert result == "Submodule2 is doing something"