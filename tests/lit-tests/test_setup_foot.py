# RUN: rm -f /root/.config/foot/foot.ini
# RUN: @python %s -m Copy | @filecheck %s

import os
import setup
import sys

if __name__ == "__main__":
    user_home = str(os.environ["HOME"])
    dir_proj = str(os.environ["PROJECT_DIR"])
    apps = [
        setup.App("Foot", os.path.join(dir_proj, "foot"), os.path.join(user_home, ".config", "foot")),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK:        Processing App:Foot(Source:/root/project/foot,Target:/root/.config/foot)
# CHECK-DAG:    Copying file /root/project/foot/foot.ini to /root/.config/foot/foot.ini
