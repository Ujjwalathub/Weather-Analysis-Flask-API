import os
import sys

# Path to your application code
path = '/home/ujjwal2112singh/API'
if path not in sys.path:
    sys.path.append(path)

# Import your Flask app
from API import app as application
