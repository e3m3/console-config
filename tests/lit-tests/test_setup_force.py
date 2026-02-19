# RUN: mkdir -p /tmp/console-config/force
# RUN: touch /tmp/console-config/force/.empty
# RUN: @python %s -m Copy         | @filecheck %s --check-prefixes=CHECK_COPY_YES,CHECK_REMOVE_NO
# RUN: @python %s -m Link         | @filecheck %s --check-prefixes=CHECK_LINK_NO,CHECK_REMOVE_NO
# RUN: @python %s -m Copy -f      | @filecheck %s --check-prefixes=CHECK_COPY_YES,CHECK_REMOVE_YES
# RUN: @python %s -m Copy --force | @filecheck %s --check-prefixes=CHECK_COPY_YES,CHECK_REMOVE_YES
# RUN: @python %s -m Link --force | @filecheck %s --check-prefixes=CHECK_LINK_YES,CHECK_REMOVE_YES

import setup
import sys

if __name__ == "__main__":
    apps = [
        setup.App("Foo", "/tmp/console-config/force", "/tmp/console-config/force-tgt"),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK_COPY_YES:       Processing App:Foo(Source:/tmp/console-config/force,Target:/tmp/console-config/force-tgt)
# CHECK_COPY_YES-DAG:   Copying file /tmp/console-config/force/.empty to /tmp/console-config/force-tgt/.empty

# CHECK_COPY_NO:        Processing App:Foo(Source:/tmp/console-config/force,Target:/tmp/console-config/force-tgt)
# CHECK_COPY_NO-NOT:    Copying file /tmp/console-config/force/.empty to /tmp/console-config/force-tgt/.empty

# CHECK_LINK_YES:       Processing App:Foo(Source:/tmp/console-config/force,Target:/tmp/console-config/force-tgt)
# CHECK_LINK_YES-DAG:   Linking file /tmp/console-config/force/.empty to /tmp/console-config/force-tgt/.empty

# CHECK_LINK_NO         Processing App:Foo(Source:/tmp/console-config/force,Target:/tmp/console-config/force-tgt)
# CHECK_LINK_NO-NOT:    Linking file /tmp/console-config/force/.empty to /tmp/console-config/force-tgt/.empty

# CHECK_REMOVE_YES-DAG: Removing existing file /tmp/console-config/force-tgt/.empty

# CHECK_REMOVE_NO-NOT:  Removing existing file /tmp/console-config/force-tgt/.empty
