"""
Why Python logging is sometimes better than print?

Because we can choose what to show! 🚀

In logging, messages like debug, info or error has specific order of importance.

If you only want to print some importance level and higher - specify this in logging config.
"""

import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Debug message")
logging.info("Info message")
