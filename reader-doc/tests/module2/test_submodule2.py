# tests/module2/test_submodule2.py
import pytest
from reader_doc.module2.submodule2 import Submodule2

@pytest.fixture
def submodule():
    return Submodule2()

def test_do_something(submodule):
    result = submodule.do_something()
    assert result == "Submodule2 is doing something"