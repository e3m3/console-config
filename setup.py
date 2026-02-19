#!/usr/bin/env python3

# Copyright 2024-2026, Giordano Salvador
# SPDX-License-Identifier: BSD-3-Clause

import os
import shutil
import sys


class App:
    NOP = 0
    COPY = 1
    LINK = 2

    def __init__(self, name: str, dir_src: str, dir_tgt: str) -> None:
        self.name = name
        self.dir_src = dir_src
        self.dir_tgt = dir_tgt

    def __str__(self) -> str:
        return f"App:{self.name}(Source:{self.dir_src},Target:{self.dir_tgt})"

    def process(self, mode: int) -> None:
        print(f"Processing {self}")
        if mode == App.NOP:
            print("[Info] No mode specified", file=sys.stderr)
            help([self], 1)
        for (path_src, path_tgt) in self.walk_source_dir():
            if not os.path.exists(path_tgt):
                # Don't overwrite existing configuration files
                dir_tgt = os.path.dirname(path_tgt)
                if not os.path.isdir(dir_tgt):
                    # Create the directories on the path to the target file along the walk
                    print(f"Creating {dir_tgt}")
                    os.makedirs(dir_tgt)
                if mode == App.COPY:
                    print(f"Copying file {path_src} to {path_tgt}")
                    shutil.copyfile(path_src, path_tgt, follow_symlinks=False)
                elif mode == App.LINK:
                    print(f"Linking file {path_src} to {path_tgt}")
                    os.symlink(path_src, path_tgt, target_is_directory=False)

    def walk_source_dir(self) -> (str, str, bool, bool):
        for (root, dirs, files) in os.walk(self.dir_src):
            is_dir: bool = len(files) == 0
            path_prefix: str = os.path.commonprefix([self.dir_src, root])
            path_middle: str = root[len(path_prefix):]
            if os.path.isabs(path_middle):
                # Remove the leading separator because join will ignore paths before "absolute" paths
                path_middle = path_middle[1:]
            for name in dirs if is_dir else files:
                path_src: str = os.path.abspath(os.path.join(root, name))
                path_tgt: str = os.path.join(self.dir_tgt, path_middle, name)
                if not is_dir:
                    yield (path_src, path_tgt)


class Args:
    class Item:
        def __init__(self) -> None:
            self.is_value: bool = False
            self.key: option[str] = None
            self.value: option[str] = None

        def clear(self) -> None:
            self.__init__()

    def __init__(self, apps: list[App], args: list[str]) -> None:
        self.help: bool = False
        self.mode: int = App.NOP
        self.app: option[str] = 'All'
        self.parse(apps, args)

    def parse(self, apps: list[App], args: list[str]) -> None:
        if len(args) < 1:
            help(apps, 1)
        item = Args.Item()
        for arg in args:
            if item.key is not None:
                item.value = arg
                _ = self.parse_key(apps, item)
                item.clear()
                continue
            arg_split = arg.strip().split('=')
            item.key = arg_split[0]
            if len(arg_split) > 1:
                item.value = arg_split[1]
            if self.parse_key(apps, item):
                continue
            item.clear()
        if item.key is not None:
            print("[Error] Unexpected end to args list", file=sys.stderr)
            sys.exit(1)

    def parse_key(self, apps: list[App], item: Item) -> None:
        """
        Update Args based on the current argument key value.
        Returns True if current argument should be shifted. Else, False.
        """
        if item.key == '-h' or item.key == '--help':
            help(apps)
        elif item.key == '-m' or item.key == '--mode':
            if item.value is None:
                return True
            elif item.value == 'Copy':
                self.mode = App.COPY
            elif item.value == 'Link':
                self.mode = App.LINK
        elif item.key == '-a' or item.key == '--app':
            if item.value is None:
                return True
            self.app = item.value if is_supported(apps, item.value) else None
        return False


def is_supported(apps: list[App], app: str) -> bool:
    return app in set([app.name for app in apps])


def help(apps: list[App], exit_code=0) -> None:
    stream = None if exit_code == 0 else sys.stderr
    print("Usage: python -m setup.py " + \
        "\n   [-h|--help] " + \
        "\n   [-m|--mode[=]<*No-op*|Copy|Link>] " + \
        f"\n   [-a|--app[=]<*All*|{'|'.join([app.name for app in apps])}>]", \
        file=stream \
    )
    sys.exit(exit_code)


def main(apps: list[App], args: Args) -> None:
    if args.app is None:
        print(f"[Error] Unknown app specified")
        sys.exit(1)
    elif args.app == 'All':
        print(f"Processing all apps: {[app.name for app in apps]}")
        for app in apps:
            app.process(args.mode)
    else:
        [app for app in apps if app.name == args.app].pop().process(args.mode)
    sys.exit(0)


if __name__ == "__main__":
    user_home: str = str(os.environ["HOME"])
    dir_curr: str = str(os.getcwd())
    apps = [
        App("Foot", os.path.join(dir_curr, "foot"), os.path.join(user_home, ".config", "foot")),
        App("Neovim", os.path.join(dir_curr, "nvim"), os.path.join(user_home, ".config", "nvim")),
        App("Qutebrowser", os.path.join(dir_curr, "qutebrowser"), os.path.join(user_home, ".config", "qutebrowser")),
        App("Sway", os.path.join(dir_curr, "sway"), os.path.join(user_home, ".config", "sway")),
        App("Tmux", os.path.join(dir_curr, "tmux"), os.path.join(user_home)),
        App("Zsh", os.path.join(dir_curr, "zsh"), os.path.join(user_home)),
    ]
    main(apps, Args(apps, sys.argv[1:]))
