#!/usr/bin/env python
import mac_wallpaper

matches = mac_wallpaper.files("Solid White.png")
if matches:
    mac_wallpaper.set(matches[0])
