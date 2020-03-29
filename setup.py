# -*- coding: utf-8 -*-
"""pylez
"""
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "pylez",
    version = "0.0.1",
    author = "Alex Fedotov",
    author_email = "alex.fedotov@aol.com",
    description = ("Rules Engine"),
    license = "MIT",
    keywords = "rules forward backward chaining",
    url = "https://github.com/alxfed/pylez",
    packages=['pylez', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
