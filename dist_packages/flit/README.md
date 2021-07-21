
# Flit
---

This example demonstrate the use of `flit`, which is a tool to build Python packages.

## Build

First, create the `pyproject.toml`
```
$ flit init
```
This will ask you some questions about the project, and create a `pyproject.toml` accordingly.

Then, you build the package:

```
$ flit build [--no-setup-py]
```

This creates a `sdist` and a wheel in the `dist` directory. 
Note that by default, the sdist will include a `setup.py` file that uses `distutils.core.setup` function. If you specify the `--no-setup-py` that file won't be generated, but then it can only be installed with tools support `PEP 517` (which uses the `pyproject.toml` rather than running `setup.py`)