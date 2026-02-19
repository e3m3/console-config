# RUN: @python %s --mode=Copy | @filecheck %s

import setup
import sys

if __name__ == "__main__":
    apps = [
        setup.App("Hello", "/tmp/foo-A", "/tmp/bar-A"),
        setup.App("World", "/tmp/foo-B", "/tmp/bar-B"),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK:    Processing all apps: ['Hello', 'World']
# CHECK:    Processing App:Hello(Source:/tmp/foo-A,Target:/tmp/bar-A)
# CHECK:    Processing App:World(Source:/tmp/foo-B,Target:/tmp/bar-B)

