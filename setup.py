#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'termplotlib',
    version = '0.0.1',
    author = 'Johan Jeppsson',
    author_email = 'johjep@gmail.com',
    description = ('Library for creating simple terminal plots'),
    license = 'GPLv3+',
    keywords = "terminal plot",
    url = 'https://github.com/johanjeppsson/termplotlib',
    packages = find_packages(),
    install_requires = ['numpy'],
    download_url = 'https://github.com/johanjeppsson/termplotlib/tarball/master',
    # TODO
    #entry_points={
    #    "console_scripts": ["drawille=drawille:__main__"]
    #},
    classifiers = [
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
