# RUN: @python %s -h     | @filecheck %s
# RUN: @python %s --help | @filecheck %s

import setup
import sys

if __name__ == "__main__":
    apps = [
        setup.App("Hello", "/tmp/foo-A", "/tmp/bar-A"),
        setup.App("World", "/tmp/foo-B", "/tmp/bar-B"),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK:    Usage: python -m setup.py
# CHECK:        [-h|--help]
# CHECK:        [-m|--mode[=]<*No-op*|Copy|Link>]
# CHECK:        [-a|--app[=]<*All*|Hello|World>]
