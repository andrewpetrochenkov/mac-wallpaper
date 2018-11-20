#!/usr/bin/env python
import mac_wallpaper

matches = mac_wallpaper.find("Solid Gray Dark.png")
if matches:
    mac_wallpaper.set(matches[0])
