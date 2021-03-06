# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_http_server",
    version="0.0.2",
    author="Keijack",
    author_email="keijack.wu@gmail.com",
    description="This is a simple http server, use MVC like design.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keijack/python-simple-http-server",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)