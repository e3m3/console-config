# RUN: @python %s | @filecheck %s

import os
import setup

if __name__ == "__main__":
    user_home: str = str(os.environ["HOME"])
    dir_proj: str = str(os.environ["PROJECT_DIR"])
    apps = [
        setup.App("Tmux", os.path.join(dir_proj, "tmux"), os.path.join(user_home)),
    ]
    setup.main(apps)

# CHECK:        Processing App:Tmux(Source:/root/project/tmux,Target:/root)
# CHECK-DAG:    Copying file /root/project/tmux/.tmux.conf to /root/.tmux.conf
