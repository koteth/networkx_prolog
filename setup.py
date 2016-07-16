#!/usr/bin/env python

from distutils.core import setup

setup(
    name='networkx_prolog',
    version='0.1',
    description='networkx Graph to prolog',
    url = '',
    scripts = [
    ],
    install_requires = ['networkx'],
    keywords = "prolog networkx graph",
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    author='Gabriele Lami',
    packages=['networkx_prolog'],
)
