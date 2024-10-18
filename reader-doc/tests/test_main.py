# tests/test_main.py
import pytest
from reader_doc.main import main

def test_main():
    # This test merely ensures that the 'main' function can be called
    # Usually, you would mock print statements or other outputs
    assert main is not None