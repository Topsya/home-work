# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import os
import sys

# sys.path.insert(0, os.path.abspath('..'))
# sys.path.insert(0, os.path.abspath('./../../jwt_na_fast_api'))
# sys.path.insert(0, os.path.abspath('./../../jwt_na_fast_api/routes'))
 
sys.path.append(os.path.abspath("jwt_na_fast_api"))


project = 'Rest API Contact'
copyright = '2023, topsya1986'
author = 'topsya1986'
release = '010'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ 'sphinx.ext.autodoc'  ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

