# RUN: rm -f /root/.zshrc
# RUN: rm -f /root/.commonrc
# RUN: @python %s -m Copy | @filecheck %s

import os
import setup
import sys

if __name__ == "__main__":
    user_home = str(os.environ["HOME"])
    dir_proj = str(os.environ["PROJECT_DIR"])
    apps = [
        setup.App("Zsh", os.path.join(dir_proj, "zsh"), os.path.join(user_home)),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK:        Processing App:Zsh(Source:/root/project/zsh,Target:/root)
# CHECK-DAG:    Copying file /root/project/zsh/.zshrc to /root/.zshrc
# CHECK-DAG:    Copying file /root/project/zsh/.commonrc to /root/.commonrc
