# reader_doc/main.py

from .module1 import Submodule1
# With absolute paths
from reader_doc.compressed import bz2_opener

def main():
    # Create instances of submodules
    submodule1 = Submodule1()
    
    # Execute methods from submodules
    print(submodule1.do_something())  # Output: Submodule1 is doing something
    print(submodule1.do_something_with_submodule2())  # Output: Submodule2 is doing something

# Can be run as below
# python3 -m reader_doc.main
if __name__ == "__main__":
    main()