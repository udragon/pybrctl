#!/usr/bin/python

from setuptools import setup, find_packages

setup(
	name = "pybrctl",
	version = "0.1",
	packages = find_packages(),
	author = "Ido Nahshon",
	author_email = "udragon@gmail.com",
	description = "Python brctl wrapper",
	license = "GPL",
	keywords = "brctl, bridge-utils",
	url = "https://github.com/udragon/pybrctl",
	long_description = open("README.md").read(),
    classifiers = ['License :: OSI Approved :: GNU General Public' +
                   'Programming Language :: Python',
                   'Operating System :: POSIX',
                   'Programming Language :: Python :: 2.7'],
 
)
