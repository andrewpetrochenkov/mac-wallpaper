import setuptools

setuptools.setup(
    name='mac-wallpaper',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/.wallpaper.applescript','scripts/wallpaper']
)
