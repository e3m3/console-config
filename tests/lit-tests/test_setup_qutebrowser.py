# RUN: rm -f /root/.config/qutebrowser/config.py
# RUN: @python %s -m Copy | @filecheck %s

import os
import setup
import sys

if __name__ == "__main__":
    user_home = str(os.environ["HOME"])
    dir_proj = str(os.environ["PROJECT_DIR"])
    apps = [
        setup.App("Qutebrowser", os.path.join(dir_proj, "qutebrowser"), os.path.join(user_home, ".config", "qutebrowser")),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK:        Processing App:Qutebrowser(Source:/root/project/qutebrowser,Target:/root/.config/qutebrowser)
# CHECK-DAG:    Copying file /root/project/qutebrowser/config.py to /root/.config/qutebrowser/config.py
