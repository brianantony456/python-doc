# reader_doc/module2/__init__.py

# Import submodule to make it accessible directly under reader_doc.module2
from .submodule2 import Submodule2

# Expose Submodule2
__all__ = ["Submodule2"]