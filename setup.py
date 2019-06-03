"""
Setup script.

:author: xarbulu
:organization: SUSE LLC
:contact: xarbulu@suse.com

:since: 2019-06-02
"""

import os

from setuptools import find_packages
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import utproject

def read(fname):
    """
    Utility function to read the README file. README file is used to create
    the long description.
    """

    return open(os.path.join(os.path.dirname(__file__), fname)).read()

VERSION = utproject.__version__
NAME = "utproject"
DESCRIPTION = "Project to show good UT practices"

AUTHOR = "xarbulu"
AUTHOR_EMAIL = "xarbulu@suse.com"
URL = ""

LICENSE = "GPL v3"

CLASSIFIERS = [

]

SCRIPTS = []

#DEPENDENCIES = read('requirements.txt').split()
DEPENDENCIES = []

PACKAGE_DATA = {}
DATA_FILES = []


SETUP_PARAMS = dict(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    long_description=read('README.md'),
    packages=find_packages(),
    package_data=PACKAGE_DATA,
    license=LICENSE,
    scripts=SCRIPTS,
    data_files=DATA_FILES,
    install_requires=DEPENDENCIES,
    classifiers=CLASSIFIERS,
)

def main():
    """
    Setup.py main.
    """

    setup(**SETUP_PARAMS)

if __name__ == "__main__":
    main()
