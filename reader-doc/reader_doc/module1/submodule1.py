# reader_doc/module1/submodule1.py
from ..module2.submodule2 import Submodule2

SUBMODULE_CONSTANT = "can't be use outside of module"

class Submodule1:
    def do_something(self):
        return "Submodule1 is doing something"

    def do_something_with_submodule2(self):
        submodule2 = Submodule2()
        return submodule2.do_something()