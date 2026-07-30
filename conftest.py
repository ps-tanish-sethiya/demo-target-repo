"""
Pytest configuration ensuring root directory is in sys.path on all platforms.
"""
import sys
import os

root_dir = os.path.abspath(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
