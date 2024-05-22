#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
# author          :Ghislain Vieilledent
# email           :ghislain.vieilledent@cirad.fr, ghislainv@gmail.com
# web             :https://ecology.ghislainv.fr
# python_version  :>=2.7
# license         :GPLv3
# ==============================================================================

import sys

import pywdpa
from .get_wdpa import get_wdpa


def main():
    """
    pywdpa.pywdpa: provides entry point main().
    """
    isocode = sys.argv[1]
    print(pywdpa.__doc__)
    print(f"version {pywdpa.__version__}.")
    print(f"Country isocode: {isocode}.")
    get_wdpa(isocode)


# End
