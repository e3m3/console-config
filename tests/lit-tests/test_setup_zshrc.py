# RUN: @python %s | @filecheck %s

import os
import setup

if __name__ == "__main__":
    user_home: str = str(os.environ["HOME"])
    dir_proj: str = str(os.environ["PROJECT_DIR"])
    apps = [
        setup.App("Zsh", os.path.join(dir_proj, "zshrc"), os.path.join(user_home)),
    ]
    setup.main(apps)

# CHECK:    Processing App:Zsh(Source:/root/project/zshrc,Target:/root)
# CHECK:    Copying file /root/project/zshrc/.zshrc to /root/.zshrc
