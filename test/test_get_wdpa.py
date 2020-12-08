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
import os.path
from pywdpa import get_wdpa


# test_get_wdpa
def test_get_wdpa():
    get_wdpa("MDG")
    assert os.path.isfile("pa_MDG.shp")

# End
