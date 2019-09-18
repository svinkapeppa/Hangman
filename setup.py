#!/usr/bin/env python3
from setuptools import setup

setup(
    name="hangman",
    version="0.0.0",
    author="Evgeny Rubanenko",
    author_email="erubanenko@gmail.com",
    url="https://github.com/svinkapeppa/hangman",
    license="MIT",
    packages=[
        "hangman",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
