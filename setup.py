#!/usr/bin/env python3

import os
import shutil


class App:
    def __init__(self, name: str, dir_src: str, dir_tgt: str) -> None:
        self.name = name
        self.dir_src = dir_src
        self.dir_tgt = dir_tgt

    def __str__(self) -> str:
        return f"App:{self.name}(Source:{self.dir_src},Target:{self.dir_tgt})"

    def walk_source(self) -> (str, str):
        user_home_abs: str = os.path.abspath(user_home)
        for f in os.walk(self.dir_src):
            for name in f[2]:
                yield (os.path.abspath(os.path.join(f[0], name)), os.path.join(self.dir_tgt, name))


def main(apps: list[App]) -> None:
    for app in apps:
        print(f"Processing {app}")
        if not os.path.isdir(app.dir_tgt):
            print(f"Creating {app.dir_tgt}")
            os.makedirs(app.dir_tgt)
        for (path_src, path_tgt) in app.walk_source():
            print(f"Copying file {path_src} to {path_tgt}")
            shutil.copyfile(path_src, path_tgt)


if __name__ == "__main__":
    user_home: str = str(os.environ["HOME"])
    dir_curr: str = str(os.getcwd())
    apps = [
        App("Neovim", os.path.join(dir_curr, "nvim"), os.path.join(user_home, ".config")),
        App("Tmux", os.path.join(dir_curr, "tmux"), os.path.join(user_home)),
        App("Zsh", os.path.join(dir_curr, "zshrc"), os.path.join(user_home)),
    ]
    main(apps)
