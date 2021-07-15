
"""
A context manager for changing directory

This script defines a function-based context manager for changing directory,
so you won't forget to change back to the previous directory. 

"""

from contextlib import contextmanager
from pathlib import Path

import os

@contextmanager
def set_directory(path: Path):
    """Sets the cwd within the context

    Args:
        path (Path): The path to the cwd

    Yields:
        None
    """

    origin = Path().absolute()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(origin)