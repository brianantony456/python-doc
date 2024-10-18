# example.py

from reader_doc import module1, module2

# Both `module1` and `module2` are accessible because they are listed in `__all__`
sub1 = module1.Submodule1()
sub2 = module2.Submodule2()

print(sub1.do_something())  # Submodule1 is doing something
print(sub2.do_something())  # Submodule2 is doing something