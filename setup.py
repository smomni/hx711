#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
from setuptools import setup, find_packages

with open(str(pathlib.Path(__file__).parent / 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hx711',
    version='1.1.2.3',
    description="A library to drive a HX711 load cell amplifier on a Raspberry Pi",
    url='https://github.com/mpibpc-mroose/hx711/',
    author="Marco Roose",
    author_email='marco.roose@gmx.de',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/mpibpc-mroose/hx711/issues',
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['tests']),
    package_data={},
    include_package_data=True,
    license="MIT license",
    keywords='hx711',
    test_suite='tests',
    extras_require={
            'dev': [],
            'test': [],
            'prod': []
    },
    scripts=['read_hx711.py'],
    entry_points={
        'console_scripts': [],
    },
)

