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
from __future__ import division, print_function  # Python 3 compatibility
import os
import requests


# get_token()
def get_token(key="WDPA_KEY"):

    """Check Protected Planet API token.

    This function checks if the user has stored a valid Protected
    Planet API token as an environment variable file under the
    key \code{WDPA_KEY}.

    Before using this package for the first time, the user must follow
    these steps: 

    1. Fill in the form available at
    <https://api.protectedplanet.net/request> to obtain a personal API
    token.

    2. Store the token as an environment variable under the key
    "WDPA_KEY". You can use the command
    os.environ["WDPA_KEY"]="your_token" or python-dotenv:
    <https://github.com/theskumar/python-dotenv>.

    :param key: Environment variable name (recommended name: "WDPA_KEY").

    :return: A vector of length one with the value of the API token.

    """

    wdpa_key = os.getenv(key)

    if wdpa_key is None:
        return ("\nMissing WDPA API token. Please ensure that:\n" +
                "1) You completed this form [https://api.protectedplanet.net/request] to get the token,\n" +
                "2) You stored the value as an environment variable with the recommended name WDPA_KEY.")

    response = requests.get("https://api.protectedplanet.net/test?token=" + wdpa_key)

    if (response.status_code == 401):
        return ("\nInvalid WDPA API token. Please ensure that:\n" +
                "1) You completed this form [https://api.protectedplanet.net/request] to get the token,\n" +
                "2) You stored the value as an environment variable with the recommended name WDPA_KEY.")

    if (response.status_code != 200):
        return "\nSomething goes wrong with your API token."

    return(wdpa_key)

# End
