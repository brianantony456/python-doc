# python-doc

This example shows a sample python packaging example

## Create a project with poetry

[Poetry Documentation](https://python-poetry.org/docs/basic-usage/)

Better virutalenvironment and package management with lock files.

```bash
poetry init                                # Initialize toml file or `poetry new project-name``
poetry config virtualenvs.in-project true  # Ensure that venv is created in project
poetry install                             # Install all the requirements in .venv folder
poetry env info                            # Get info about the project
poetry add|remove jinja2                   # Add and install a specific package
poetry shell                               # Activate virtual environment
exit                                       # Exit shell
``` 