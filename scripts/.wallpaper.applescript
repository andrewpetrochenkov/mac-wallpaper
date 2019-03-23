#!/usr/bin/osascript

on run argv
    if count of argv is 1 then -- set
        tell application "System Events"
            tell every desktop
                set picture to (item 1 of argv as POSIX FILE)
            end tell
        end tell
    else -- get
        tell application "System Events" to tell every desktop to picture
    end if
end run
