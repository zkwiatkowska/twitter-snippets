"""
Creating a path using Python is really easy with pathlib. 🚀

You can additionally specify:
🔁 parents=True - to create all missing directories in a path,
🆗 exists_ok=True - to ignore the fact the path already exists.

Default is False for both parameters.
"""

from pathlib import Path

outputs = Path('outputs/experiment1')
outputs.mkdir(parents=True, exist_ok=True)
