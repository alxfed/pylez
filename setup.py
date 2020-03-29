# -*- coding: utf-8 -*-
"""pylez
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylez",
    version="0.0.1",
    author="Alex Fedotov",
    author_email="alex.fedotov@aol.com",
    description="Rules Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alxfed/pylez",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
