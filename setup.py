#!/usr/bin/env python
from setuptools import setup, find_packages
import itertools
from physt import __version__

options = dict(
    name='physt',
    version=__version__,
    packages=find_packages(),
    license='MIT',
    description='',
    long_description=open('README.md').read(),
    author='Jan Pipek',
    author_email='jan.pipek@gmail.com',
    url='https://github.com/janpipek/physt',
    install_requires = ['numpy'],
    extras_require = {
        # 'all' : []
    },
    entry_points = {
        'console_scripts' : [
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)

extras = options['extras_require']
extras['full'] = list(set(itertools.chain.from_iterable(extras.values())))
setup(**options)