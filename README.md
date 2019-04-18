<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-wallpaper.svg?longCache=True)](https://pypi.org/project/mac-wallpaper/)
[![](https://img.shields.io/pypi/v/mac-wallpaper.svg?maxAge=3600)](https://pypi.org/project/mac-wallpaper/)
[![](https://img.shields.io/npm/v/mac-wallpaper.svg?maxAge=3600)](https://www.npmjs.com/package/mac-wallpaper)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-wallpaper.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-wallpaper.py/)

#### Installation
```bash
$ [sudo] npm i -g mac-wallpaper
```
```bash
$ [sudo] pip install mac-wallpaper
```

#### Functions
function|`__doc__`
-|-
`mac_wallpaper.get()` |return wallpaper path
`mac_wallpaper.update(path)` |update wallpaper path

#### Scripts usage
```bash
usage: wallpaper [path]
```

#### Examples
```python
>>> import mac_wallpaper
>>> mac_wallpaper.update('path/to/wallpaper.jpg')
>>> mac_wallpaper.get()
'path/to/wallpaper.jpg'
```

```bash
$ wallpaper path/to/wallpaper.jpg
$ wallpaper
path/to/wallpaper.jpg
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>