"""
Want to list all .py files recursively in directory and its subdirectories?

Use pathlib! 🚀

Pathlib provides very convenient *glob* method to search for a given *file pattern* within a path you're interested into.
"""

from pathlib import Path

my_path = Path("some/path/with/subdirectories")
all_py_files = list(my_path.glob(f'**/*.py'))
