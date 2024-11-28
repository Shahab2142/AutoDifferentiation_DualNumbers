# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'dual_autodiff'
copyright = '2024, Shahab Yousef-Nasiri'
author = 'Shahab Yousef-Nasiri'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  
    'sphinx.ext.napoleon',  
]


templates_path = ['_templates']


exclude_patterns = []


import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Use the ReadTheDocs theme (better for readability)
html_theme = 'sphinx_rtd_theme'

# List of paths that contain custom static files (such as CSS).
html_static_path = ['_static']
