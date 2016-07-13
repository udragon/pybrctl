#!/usr/bin/python

from setuptools import setup, find_packages

setup(
	name = "pybrctl",
	version = "0.1.3",
	packages = find_packages(),
	author = "Ido Nahshon",
	author_email = "udragon@gmail.com",
	description = "Python brctl wrapper",
	license = "GPLv2",
	keywords = "brctl, bridge-utils",
	url = "https://github.com/udragon/pybrctl",
	long_description = open("README.rst").read(),
    classifiers = ['License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                   'Programming Language :: Python',
                   'Operating System :: POSIX',
                   'Programming Language :: Python :: 2.7'],
 
)
