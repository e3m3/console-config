# RUN: @python %s -a World -m Copy | @filecheck %s
# RUN: @python %s -a World -m=Copy | @filecheck %s
# RUN: @python %s -a=World -m Copy | @filecheck %s
# RUN: @python %s -a=World -m=Copy | @filecheck %s
# RUN: @python %s --app World --mode Copy | @filecheck %s
# RUN: @python %s --app=World --mode Copy | @filecheck %s
# RUN: @python %s --app World --mode=Copy | @filecheck %s
# RUN: @python %s --app=World --mode=Copy | @filecheck %s

import setup
import sys

if __name__ == "__main__":
    apps = [
        setup.App("Hello", "/tmp/foo-A", "/tmp/bar-A"),
        setup.App("World", "/tmp/foo-B", "/tmp/bar-B"),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK:    Processing App:World(Source:/tmp/foo-B,Target:/tmp/bar-B)
