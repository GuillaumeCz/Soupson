#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages 

setup(
    name="soupson",
    version="0.0.1",
    description="Soupson quoi...",
    author="GuillaumeCz",
    install_requires=[
        'requests',
        'bs4'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'soupson=soupson.soupson:main'
        ]
    }
)
