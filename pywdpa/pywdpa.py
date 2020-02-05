#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
# author          :Ghislain Vieilledent
# email           :ghislain.vieilledent@cirad.fr, ghislainv@gmail.com
# web             :https://ecology.ghislainv.fr
# python_version  :>=2.7
# license         :GPLv3
# ==============================================================================

"""pywdpa.pywdpa: provides entry point main()."""

__version__ = "0.1.1"

import sys
from .get_wdpa import get_wdpa

def main():
    print("Executing pywdpa version %s." % __version__)
    print("For country with isocode: %s" % sys.argv[1])
    get_wdpa(sys.argv[1])
    return None

# End
