#!/usr/bin/env python
import sys
from os.path import abspath, dirname, join
from django.core.management import execute_manager

# Since the palette app is located in the parent directory, we'll have
# to add that to the PYTHONPATH
PROJECT_ROOT = abspath(dirname(__file__))
sys.path.insert(0, join(PROJECT_ROOT, "../"))

try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
