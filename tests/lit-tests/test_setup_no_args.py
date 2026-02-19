# RUN: not @python %s 2>&1 | @filecheck %s

import setup

if __name__ == "__main__":
    apps = []
    setup.main(apps, setup.Args(apps, []))

# CHECK:    Usage: python -m setup.py
