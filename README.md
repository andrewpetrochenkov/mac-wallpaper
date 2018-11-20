[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-wallpaper.svg?longCache=True)](https://pypi.org/pypi/mac-wallpaper/)
[![](https://img.shields.io/pypi/v/mac-wallpaper.svg?maxAge=3600)](https://pypi.org/pypi/mac-wallpaper/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-wallpaper.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-wallpaper.py/)

#### Install
```bash
$ [sudo] pip install mac-wallpaper
```

#### Functions
function|description
-|-
`mac_wallpaper.get()`|return wallpaper path
`mac_wallpaper.update(path)`|update wallpaper path

#### CLI
usage|description
-|-
`python -m mac_wallpaper [path]`|get/set wallpaper path

#### Examples
```python
>>> import mac_wallpaper
>>> mac_wallpaper.update('path/to/wallpaper.jpg')
>>> mac_wallpaper.get()
'path/to/wallpaper.jpg'
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>