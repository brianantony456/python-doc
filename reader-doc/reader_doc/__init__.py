# reader_doc/__init__.py

# Expose module1 and module2 when the package is imported
__all__ = ["module1", "module2"]

# Import submodules to make them accessible directly under reader_doc
from .module1.submodule1 import Submodule1
from .module2.submodule2 import Submodule2