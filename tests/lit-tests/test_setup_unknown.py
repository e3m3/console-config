# RUN: not @python %s -a Super -m Copy 2>&1 | @filecheck %s
# RUN: not @python %s -a       -m Copy 2>&1 | @filecheck %s
# RUN: not @python %s -a=      -m Copy 2>&1 | @filecheck %s

import setup
import sys

if __name__ == "__main__":
    apps = [
        setup.App("Hello", "/tmp/foo-A", "/tmp/bar-A"),
        setup.App("World", "/tmp/foo-B", "/tmp/bar-B"),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK:    [Error] Unknown app specified
