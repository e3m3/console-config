# RUN: mkdir -p /tmp/console-config/link
# RUN: touch /tmp/console-config/link/.empty
# RUN: @python %s -m Link | @filecheck %s

import setup
import sys

if __name__ == "__main__":
    apps = [
        setup.App("Foo", "/tmp/console-config/link", "/tmp/console-config/link-tgt"),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK:        Processing App:Foo(Source:/tmp/console-config/link,Target:/tmp/console-config/link-tgt)
# CHECK-DAG:    Linking file /tmp/console-config/link/.empty to /tmp/console-config/link-tgt/.empty
# CHECK-NOT:    Copying file /tmp/console-config/link/.empty to /tmp/console-config/link-tgt/.empty
