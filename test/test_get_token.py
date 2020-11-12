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
from pywdpa import get_token


# test_get_token
def test_get_token():
    token = get_token(key="")
    msg = ("Missing WDPA API token. Please ensure that:{sep}"
           "1) You completed this form [https://api.protectedplanet.net/request] "
           "to get the token.{sep}"
           "2) You stored the value as an environment variable with the "
           "recommended name WDPA_KEY.").format(sep="\n")
    assert token == msg

# End
