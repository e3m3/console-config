# RUN: rm -f /root/.tmux.conf
# RUN: @python %s -m Link | @filecheck %s

import os
import setup
import sys

if __name__ == "__main__":
    user_home = str(os.environ["HOME"])
    dir_proj = str(os.environ["PROJECT_DIR"])
    apps = [
        setup.App("Tmux", os.path.join(dir_proj, "tmux"), os.path.join(user_home)),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK:        Processing App:Tmux(Source:/root/project/tmux,Target:/root)
# CHECK-DAG:    Linking file /root/project/tmux/.tmux.conf to /root/.tmux.conf
