# SamplePythonToolbox
Sample ArcGIS Pro Python Toolbox

Testing distributing geoprocessing toolboxes with Python modules and how to build on GitHub.


## Line Length

Line length needs to be consistently configured for formatting, linting and while sorting imports. In order to change the line length for a specific project, it will need to be updated in the following locations:

- `.pylintrc`
- `pyproject.toml`

## Formatting

Formatting is handled by `black`.

Black is an uncompromising Python code formatting tool. It takes a Python file as an input, and provides a reformatted Python file as an output, using rules that are a strict subset of [PEP 8](https://www.python.org/dev/peps/pep-0008/). It offers very little in the way of configuration (line length being the main exception) in order to achieve formatting consistency. It is deterministic - it will always produce the same output from the same inputs.

The line length configuration is stored in `pyproject.toml`.

Configuring Black to automatically run every time code is modified allows developers to forget about _how_ code should be formatted and stay focused on functionality. Many IDEs and text editors allow this. Git hooks can also be used to execute Black before Python code is committed to a repository - this is not configured here as use of autosave and continuous integration checks makes it redundant.

### VSCode Configuration

In VSCode, you can set the default Python formatter using the setting: `"python.formatting.provider": "black"`, and then turn on autosave using `"editor.formatOnSave": true`. VSCode will pick up the line length configuration from a `pyproject.toml` file per repository.

## Sorting Imports

Import sorting is handled by `isort`.

isort sorts Python imports alphabetically within their respective sections:

1. Standard library imports
2. Related third party imports
3. Local application / library specific imports

isort has many configuration options but these can cause inconsistencies with Black, so must be carefully assessed. The configurations within this repository will provide consistently ordered / formatted imports.

The configuration is stored in `pyproject.toml`.

### VSCode Configuration
VSCode will pick up the isort configuration from a `pyproject.toml` file per repository.
It is possible to configure VSCode to run `isort` every time you save, using the `codeActionsOnSave": { "source.organizeImports": true }` setting. This currently causes a race condition when formatting by `black` is also configured to occur on save (`"editor.formatOnSave": true`), leading to lines being erroneously deleted. The VSCode Python team [can't do anything](https://github.com/Microsoft/vscode-python/issues/2301) about this.

The configuration stored here works with `black` - that is to say, `black` will not reformat changes made by `isort` - but it is still unsafe to apply both commands simultaneously.

In VSCode, you can manually trigger import sorting by:

- right clicking anywhere within a file and selecting `Sort Imports`.
- command palette (`Ctrl + Shift + P`), then `Python Refactor: Sort Imports`.
- creating a shortcut key for `python.sortImports`

## Linting

Linting is handled by `pylint`.

Pylint checks Python files in order to detect syntax errors and potential bugs (unreachable code / unused variables), provide refactoring help,

The configuration is stored in `.pylintrc`.

