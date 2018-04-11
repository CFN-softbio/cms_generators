#!/usr/bin/env python

import setuptools
from distutils.core import setup, Extension
import os
import sys
import importlib

# Install required dependencies before setup()
deps = {
        'numpy': {
            'module': 'numpy',
            'function': None,
            'alias': 'np'
            },
        }


def _import(module, function=None, alias=None):
    if function:
        globals()[function] = getattr(importlib.import_module(module), function)
    if alias:
        globals()[alias] = importlib.import_module(module)


for lib, dep in deps.items():
    try:
        _import(**dep)
    except ImportError:
        import pip
        pip.main(['install', lib])
        _import(**dep)

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='cms_generators',
    author='Brookhaven National Lab',
    description="Data simulators",
    packages=setuptools.find_packages(exclude=['doc']),
    include_dirs=[np.get_include()],
    package_data={'cms_generators.tools.xraydb.db': ['tools/xraydb/db/*']},
    install_requires=['six', 'numpy'],  # essential deps only
    url='http://github.com/CFN-softbio/cms_generators',
    keywords='Xray Analysis',
    license='BSD',
    classifiers=['Development Status :: 3 - Alpha',
                 "License :: OSI Approved :: BSD License",
                 "Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3.4",
                 "Topic :: Scientific/Engineering :: Physics",
                 "Topic :: Scientific/Engineering :: Chemistry",
                 "Topic :: Software Development :: Libraries",
                 "Intended Audience :: Science/Research",
                 "Intended Audience :: Developers",
                 ],
    )
