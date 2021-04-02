from setuptools import setup

setup(
    name="atree",  #pypi中的名称，pip或者easy_install安装时使用的名称，或生成egg文件的名称
    version="0.0.1",
    packages=['src'],  # 需要打包的目录列表

    # 需要安装的依赖
    install_requires=[],
    # 添加这个选项，在windows下Python目录的scripts下生成exe文件
    # 注意：模块与函数之间是冒号:
    entry_points={'console_scripts': [
        'atree = src.run:main',
    ]},
    # 此项需要，否则卸载时报windows error
    zip_safe=False
)