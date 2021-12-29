from pathlib import Path

my_path = Path("some/path/with/subdirectories")
all_py_files = list(my_path.glob(f'**/*.py'))
