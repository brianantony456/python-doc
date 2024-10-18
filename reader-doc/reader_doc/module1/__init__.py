# reader_doc/module1/__init__.py

# Import submodule to make it accessible directly under reader_doc.module1 without submodule1
from .submodule1 import Submodule1

# Expose Submodule1
__all__ = ["Submodule1"]