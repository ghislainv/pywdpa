# pywdpa Python package

## Overview

The `pywdpa` Python package is an interface to the World Database on Protected Areas (WDPA) hosted on the Protected Planet website at <https://www.protectedplanet.net>. The `pywdpa` package provides functions to download shapefiles of protected areas (PA) for any countries with an iso3 code using the WDPA API at <https://api.protectedplanet.net>. The `pywdpa` package translates some functions of the R package `worldpa` (<https://github.com/FRBCesab/worldpa>) in the Python language.

## Terms and conditions

You must ensure that the following citation is always clearly reproduced in any publication or analysis involving the Protected Planet Materials in any derived form or format:

> UNEP-WCMC and IUCN (`YEAR`) Protected Planet: The World Database on Protected Areas (WDPA). Cambridge, UK: UNEP-WCMC and IUCN. Available at: www.protectedplanet.net (dataset downloaded the `YEAR/MONTH`).

For further details on terms and conditions of the WDPA usage, please visit the page: <https://www.protectedplanet.net/c/terms-and-conditions>.

## Prerequisites

This package uses the WDPA API to access data on world protected areas. You must first have obtained a Personal API Token by filling in the form available at <https://api.protectedplanet.net/request>. Then set an environment variable (we recommend using the name `WDPA_KEY`) using either the command `os.environ["WDPA_KEY"]="your_token"` or [python-dotenv](https://github.com/theskumar/python-dotenv).

## Installation

The easiest way to install the `pywdpa` Python package is via [pip](https://pip.pypa.io/en/stable/):

```
~$ python -m pip install --upgrade https://github.com/ghislainv/pywdpa/archive/master.zip
```

but you can also install it executing the `setup.py` file:

```
~$ git clone https://github.com/ghislainv/pywdpa
~$ cd pywdpa
~/pywdpa$ python setup.py install
```
