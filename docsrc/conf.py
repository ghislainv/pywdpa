# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re  # Regular expression
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'pywdpa'
copyright = '2020, Ghislain Vieilledent'
author = 'Ghislain Vieilledent'

# The full version, including alpha/beta/rc tags
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('../pywdpa/pywdpa.py').read(),
    re.M
    ).group(1)
release = version

# -- Sphynx options ----------------------------------------------------------
add_module_names = False
add_function_parentheses = True

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode',
              'sphinx.ext.napoleon', 'sphinx.ext.mathjax', 'nbsphinx']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'  # 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'description': "A simple access to world's protected areas",
    'code_font_family': "'Roboto Mono', 'Consolas', 'Menlo', "
                        "'Deja Vu Sans Mono', "
                        "'Bitstream Vera Sans Mono', monospace",
    'font_family': "'Lato', Arial, sans-serif",
    'head_font_family': "'Lato', Arial, sans-serif",
    'body_text': '#000',
    'sidebar_header': '#4B4032',
    'sidebar_text': '#49443E',
    'github_banner': 'false',
    'github_user': 'ghislainv',
    'github_repo': 'pywdpa',
    'github_button': 'true',
    'github_type': 'star',
    'travis_button': 'false',
    'codecov_button': 'false',
    'logo': 'logo-pywdpa.svg'
}
html_favicon = '_static/favicon.ico'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# End of file
