from setuptools import setup

setup(
    name="atree",  # lib name
    version="0.0.1",
    packages=['src'],  # which package to include
    install_requires=[],
    # use entry_points to generate cli command file or .exe on windows
    entry_points={'console_scripts': [
        'atree = src.run:main',
    ]},
    # for windows, if not will show error when uninstall
    zip_safe=False
)