from pathlib import Path

my_path = Path("my_directory/")
path_to_subdirectory = my_path / "my_subdirectory"

print(path_to_subdirectory)  # this results in: "my_path/my_subdirectory"
