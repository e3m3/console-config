# RUN: not @python %s -a World     2>&1 | @filecheck %s
# RUN: not @python %s -a World -m= 2>&1 | @filecheck %s

import setup
import sys

if __name__ == "__main__":
    apps = [
        setup.App("Hello", "/tmp/foo-A", "/tmp/bar-A"),
        setup.App("World", "/tmp/foo-B", "/tmp/bar-B"),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK:    [Info] No mode specified
# CHECK:    Usage: python -m setup.py
