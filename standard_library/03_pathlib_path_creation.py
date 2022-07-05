"""
Pathlib is an awesome way to keep your code cleaner when you work with paths.

One of the examples is joining paths.

In order to add a subdirectory to a path, you simply use "/" operator to join them.
"""

from pathlib import Path

my_path = Path("my_directory/")
path_to_subdirectory = my_path / "my_subdirectory"

print(path_to_subdirectory)  # this results in: "my_path/my_subdirectory"
