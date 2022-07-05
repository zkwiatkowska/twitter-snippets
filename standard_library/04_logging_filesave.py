"""
Creating logs is really important when conducting an ML experiment.

One of the ways to do this that is built in pure Python is logging with save to file option. 🚀

Of course the con of this approach is that we can only save text messages, but the pro - it is extremely simple!
"""

import logging

logging.basicConfig(filename='my_logs.log', level=logging.INFO)
logging.info('This will be saved in my logs file that I can keep')
