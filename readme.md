example to show how to use python to build a cli tool

implement a tree method as atree and use setuptools to build a cli tool which will work like follow
```bash
$ atree . 
└─atree
  ├─readme.md
  ├─setup.py
  └─src
    ├─run.py
    ├─__pycache__
    │ └─atree.cpython-39.pyc
    └─atree.py
```

use setuptools to generate execute file
```python
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
```


caution:

1. for positional args, use nargs='?' to set default value if not provided on command line
   
    `parser.add_argument('file', nargs='?', default=".")`

2. carefully deal with module import
   
    https://zhuanlan.zhihu.com/p/69099185

