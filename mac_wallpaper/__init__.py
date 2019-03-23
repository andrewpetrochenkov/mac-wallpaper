#!/usr/bin/env python
"""get/update wallpaper path"""
import applescript
import public


@public.add
def get():
    """return wallpaper path"""
    return applescript.tell.app("System Events", "tell every desktop to picture").out


@public.add
def update(path):
    """update wallpaper path"""
    applescript.tell.app("System Events", """tell every desktop
    set picture to ("%s" as POSIX FILE)
end tell""" % path)
