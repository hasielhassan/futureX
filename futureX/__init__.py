import os
import sys

def get_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    if sys.version_info[:2] < (3, 0):
        future_path = os.path.join(current_dir, 'python2')
    else:
        future_path = os.path.join(current_dir, 'python3')

sys.path.append(get_path())