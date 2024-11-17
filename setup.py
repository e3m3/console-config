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
        for f in os.walk(self.dir_src):
            is_dir: bool = len(f[2]) == 0
            path_prefix: str = os.path.commonprefix([self.dir_src, f[0]])
            path_middle: str = f[0][len(path_prefix):]
            if os.path.isabs(path_middle):
                # Remove the leading separator because join will ignore paths before "absolute" paths
                path_middle = path_middle[1:]
            for name in f[1] if is_dir else f[2]:
                path_src: str = os.path.abspath(os.path.join(f[0], name))
                path_tgt: str = os.path.join(self.dir_tgt, path_middle, name)
                yield (path_src, path_tgt, is_dir)


def main(apps: list[App]) -> None:
    for app in apps:
        print(f"Processing {app}")
        if not os.path.isdir(app.dir_tgt):
            print(f"Creating {app.dir_tgt}")
            os.makedirs(app.dir_tgt)
        for (path_src, path_tgt, is_dir) in app.walk_source():
            if is_dir and not os.path.isdir(path_tgt):
                print(f"Creating {path_tgt}")
                os.makedirs(path_tgt)
            elif not is_dir and not os.path.exists(path_tgt):
                # Don't overwrite existing configuration files
                print(f"Copying file {path_src} to {path_tgt}")
                shutil.copyfile(path_src, path_tgt)


if __name__ == "__main__":
    user_home: str = str(os.environ["HOME"])
    dir_curr: str = str(os.getcwd())
    apps = [
        App("Neovim", os.path.join(dir_curr, "nvim"), os.path.join(user_home, ".config", "nvim")),
        App("Tmux", os.path.join(dir_curr, "tmux"), os.path.join(user_home)),
        App("Zsh", os.path.join(dir_curr, "zshrc"), os.path.join(user_home)),
    ]
    main(apps)
