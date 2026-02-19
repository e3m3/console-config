# RUN: rm -f /root/.config/sway/config
# RUN: rm -f /root/.config/sway/waybar/config.jsonc
# RUN: rm -f /root/.config/sway/waybar/style.css
# RUN: @python %s -m Copy | @filecheck %s

import os
import setup
import sys

if __name__ == "__main__":
    user_home = str(os.environ["HOME"])
    dir_proj = str(os.environ["PROJECT_DIR"])
    apps = [
        setup.App("Sway", os.path.join(dir_proj, "sway"), os.path.join(user_home, ".config", "sway")),
    ]
    setup.main(apps, setup.Args(apps, sys.argv[1:]))

# CHECK:        Processing App:Sway(Source:/root/project/sway,Target:/root/.config/sway)
# CHECK-DAG:    Copying file /root/project/sway/config to /root/.config/sway/config
# CHECK-DAG:    Copying file /root/project/sway/waybar/config.jsonc to /root/.config/sway/waybar/config.jsonc
# CHECK-DAG:    Copying file /root/project/sway/waybar/style.css to /root/.config/sway/waybar/style.css
