#!/usr/bin/env bash
{ set +x; } 2>/dev/null

image="$(find "/Library/Desktop Pictures" -name "*.jpg" | head -1)" || exit
( set -x; wallpaper "$image" ) || exit
( set -x; wallpaper )

