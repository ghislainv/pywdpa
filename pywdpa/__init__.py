"""
pywdpa: Easy access to world's protected areas.
https://ecology.ghislainv.fr/pywdpa/
"""

# Define double undescore variables
# https://peps.python.org/pep-0008/#module-level-dunder-names
__author__ = "Ghislain Vieilledent"
__email__ = "ghislain.vieilledent@cirad.fr"
__version__ = "0.1.6"

# GDAL exceptions
from osgeo import gdal

from .get_token import get_token
from .get_wdpa import get_wdpa

# GDAL exceptions
gdal.UseExceptions()

# End
