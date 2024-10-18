# Documentation

Detailed documentation for the Reader Doc project.

## Design of the project

```bash
reader-doc/
├── .git/
├── .gitignore
├── pyproject.toml
├── README.md
├── Makefile
├── docs/
│   └── index.md
├── reader_doc/
│   ├── __init__.py
│   ├── main.py
│   ├── __main__.py
│   ├── module1/
│   │   ├── __init__.py
│   │   └── submodule1.py
│   ├── module2/
│   │   ├── __init__.py
│   │   └── submodule2.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
│   ├── module1/
│   │   ├── __init__.py
│   │   └── test_submodule1.py
│   ├── module2/
│   │   ├── __init__.py
│   │   └── test_submodule2.py
```