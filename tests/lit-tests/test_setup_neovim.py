# RUN: rm -f /root/.config/nvim/init.lua
# RUN: rm -f /root/.config/nvim/lua/config/lazy.lua
# RUN: rm -f /root/.config/nvim/lua/plugins/codecompanion.lua
# RUN: @python %s -m Copy | @filecheck %s

import os
import setup
import sys

if __name__ == "__main__":
    user_home = str(os.environ["HOME"])
    dir_proj = str(os.environ["PROJECT_DIR"])
    apps = [
        setup.App("Neovim", os.path.join(dir_proj, "nvim"), os.path.join(user_home, ".config", "nvim")),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK:        Processing App:Neovim(Source:/root/project/nvim,Target:/root/.config/nvim)
# CHECK-DAG:    Copying file /root/project/nvim/init.lua to /root/.config/nvim/init.lua
# CHECK-DAG:    Copying file /root/project/nvim/lua/config/lazy.lua to /root/.config/nvim/lua/config/lazy.lua
# CHECK-DAG:    Copying file /root/project/nvim/lua/plugins/codecompanion.lua to /root/.config/nvim/lua/plugins/codecompanion.lua
