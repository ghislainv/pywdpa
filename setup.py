#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
# author          :Ghislain Vieilledent
# email           :ghislain.vieilledent@cirad.fr, ghislainv@gmail.com
# web             :https://ecology.ghislainv.fr
# python_version  :>=2.7
# license         :GPLv3
# ==============================================================================

# Import
from setuptools import setup

# Markdown README file
with open("README.md", "r") as fh:
    long_description = fh.read()

# Setup
setup(name="pywdpa",
      version="0.1",
      author="Ghislain Vieilledent",
      author_email="ghislain.vieilledent@cirad.fr",
      url="https://github.com/ghislainv/wdpa",
      license="GPLv3",
      description="This is the Python 'pywdpa' package",
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=["Development Status :: 4 - Beta",
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 3",
                   "Operating System :: OS Independent",
                   "Topic :: Scientific/Engineering :: Bio-Informatics"],
      keywords="protected areas wdpa world database on protected areas",
      python_requires=">=2.7",
      packages=["pywdpa"],
      package_dir={"pywdpa": "pywdpa"},
      install_requires=["numpy", "gdal", "requests", "dotenv"],
      zip_safe=False)

# End
