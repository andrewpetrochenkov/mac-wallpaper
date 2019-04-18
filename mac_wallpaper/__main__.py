#!/usr/bin/env python
"""get/set macOS wallpaper"""
import click
import mac_wallpaper

MODULE_NAME = "mac_wallpaper"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [path]' % MODULE_NAME


@click.command()
@click.argument('path', required=False)
def _cli(path=None):
    if path is not None:
        mac_wallpaper.update(path)
    else:
        print(mac_wallpaper.get())


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
