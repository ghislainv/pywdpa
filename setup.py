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
import re  # Regular expression
from setuptools import setup

# Version
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('pywdpa/pywdpa.py').read(),
    re.M
    ).group(1)

# reStructuredText README file
with open("README.rst", "rb") as f:
    long_description = f.read().decode("utf-8")

# Project URLs
project_urls = {
    'Documentation': 'https://ecology.ghislainv.fr/pywdpa',
    'Source': 'https://github.com/ghislainv/pywdpa/',
    'Traker': 'https://github.com/ghislainv/pywdpa/issues',
}

# Setup
setup(name="pywdpa",
      version=version,
      author="Ghislain Vieilledent",
      author_email="ghislain.vieilledent@cirad.fr",
      url="https://ecology.ghislainv.fr/pywdpa",
      project_urls=project_urls,
      license="GPLv3",
      description="Easy access to world's protected areas",
      long_description=long_description,
      long_description_content_type="text/x-rst",
      classifiers=["Development Status :: 4 - Beta",
                   "License :: OSI Approved :: GNU General Public License v3 "
                   "(GPLv3)",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 3",
                   "Operating System :: OS Independent",
                   "Topic :: Scientific/Engineering :: Bio-Informatics"],
      keywords="protected areas wdpa world database protected areas",
      python_requires=">=2.7",
      packages=["pywdpa"],
      package_dir={"pywdpa": "pywdpa"},
      entry_points={"console_scripts": ["pywdpa = pywdpa.pywdpa:main"]},
      install_requires=["numpy", "gdal", "requests"],
      extras_require={
          "interactive": ["jupyter", "python-dotenv", "geopandas",
                          "descartes", "folium"]},
      zip_safe=False)

# End
