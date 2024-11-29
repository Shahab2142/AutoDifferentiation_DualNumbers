# Configuration file for the Sphinx documentation builder.
# Full documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath('../../../../dual_autodiff'))


# -- Project information -----------------------------------------------------
project = 'dual_autodiff'
copyright = '2024, Shahab Yousef-Nasiri'
author = 'Shahab Yousef-Nasiri'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',      
    'sphinx.ext.napoleon',     

]

# Templates path
templates_path = ['_templates']

# Exclude patterns
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  
html_static_path = ['_static']  
