..
   # ==============================================================================
   # author          :Ghislain Vieilledent
   # email           :ghislain.vieilledent@cirad.fr, ghislainv@gmail.com
   # web             :https://ecology.ghislainv.fr
   # license         :GPLv3
   # ==============================================================================

.. image:: https://ecology.ghislainv.fr/pywdpa/_static/logo-pywdpa.svg
   :align: right
   :target: https://ecology.ghislainv.fr/pywdpa
   :alt: Logo pywdpa
   :width: 140px
	   
``pywdpa`` Python package
*************************


|Python version| |PyPI version| |GitHub Actions| |License| |Zenodo|


Overview
========

The ``pywdpa`` Python package is an interface to the World Database on
Protected Areas (WDPA) hosted on the Protected Planet website at
`<https://www.protectedplanet.net>`_. The ``pywdpa`` package provides
functions to download shapefiles of protected areas (PA) for any
countries with an iso3 code using the Protected Planet API at
`<https://api.protectedplanet.net>`_. The ``pywdpa`` package
translates some functions of the R package ``worldpa``
(`<https://github.com/FRBCesab/worldpa>`_) in the Python language.

.. image:: https://ecology.ghislainv.fr/pywdpa/_static/banner_pywdpa.png
   :align: center
   :target: https://ecology.ghislainv.fr/pywdpa
   :alt: protected-planet

Terms and conditions
====================

You must ensure that the following citation is always clearly
reproduced in any publication or analysis involving the Protected
Planet Materials in any derived form or format:

..
   
    UNEP-WCMC and IUCN (\ ``YEAR``\ ) Protected Planet: The World
    Database on Protected Areas (WDPA). Cambridge, UK: UNEP-WCMC and
    IUCN. Available at: www.protectedplanet.net (dataset downloaded the
    ``YEAR/MONTH``\ ).


For further details on terms and conditions of the WDPA usage, please
visit the page: `<https://www.protectedplanet.net/en/legal>`_.

Prerequisites
=============

This package uses the Protected Planet API to access data on world
protected areas. You must first have obtained a Personal API Token by
filling in the form available at
`<https://api.protectedplanet.net/request>`_. Then you need to set an
environment variable (we recommend using the name ``WDPA_KEY``\ )
using either the command ``os.environ["WDPA_KEY"]="your_token"`` or
`python-dotenv <https://github.com/theskumar/python-dotenv>`_.

Installation
============

The easiest way to install the ``pywdpa`` Python package is via `pip <https://pip.pypa.io/en/stable/>`_:

.. code-block:: bash

   $ # For version on PyPI
   $ python -m pip install pywdpa

or 

.. code-block:: bash

   $ # For development version on GitHub
   $ python -m pip install https://github.com/ghislainv/pywdpa/archive/master.zip

but you can also install ``pywdpa`` executing the ``setup.py`` file:

.. code-block:: bash

   $ git clone https://github.com/ghislainv/pywdpa
   $ cd pywdpa
   $ python setup.py install

Contributing
============

The ``pywdpa`` Python package is Open Source and released under
the `GNU GPL version 3 license
<https://ecology.ghislainv.fr/pywdpa/license.html>`__. Anybody
who is interested can contribute to the package development following
our `Community guidelines
<https://ecology.ghislainv.fr/pywdpa/contributing.html>`__. Every
contributor must agree to follow the project's `Code of conduct
<https://ecology.ghislainv.fr/pywdpa/code_of_conduct.html>`__.
   
.. |Python version| image:: https://img.shields.io/pypi/pyversions/pywdpa?logo=python&logoColor=ffd43b&color=306998
   :target: https://pypi.org/project/pywdpa
   :alt: Python version

.. |PyPI version| image:: https://img.shields.io/pypi/v/pywdpa
   :target: https://pypi.org/project/pywdpa
   :alt: PyPI version

.. |GitHub Actions| image:: https://github.com/ghislainv/pywdpa/workflows/PyPkg/badge.svg
   :target: https://github.com/ghislainv/pywdpa/actions
   :alt: GitHub Actions
	 
.. |License| image:: https://img.shields.io/badge/licence-GPLv3-8f10cb.svg
   :target: https://www.gnu.org/licenses/gpl-3.0.html
   :alt: License GPLv3

.. |Zenodo| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.4275513.svg
   :target: https://doi.org/10.5281/zenodo.4275513
   :alt: Zenodo

