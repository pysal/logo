__version__ = "0.0.2"
"""
:mod:`logo` --- logo generation for the PySAL project
=====================================================
"""
from .create_pysal_logo import create_logo, create_favicon

from .predefined import CHILD_NODES, GRANDCHILD_NODES
from .predefined import NO_TEXT, GREEK, BULLETS
from .predefined import WHITE, BLACK, DARKGRAY
from .predefined import traditional_theme_light, traditional_theme_dark
from .predefined import canon2020_theme_light, canon2020_theme_dark
from .predefined import cb_qual_Paired_n7_theme_light, cb_qual_Paired_n7_theme_dark
from .predefined import cb_qual_Set1_n7_theme_light, cb_qual_Set1_n7_theme_dark
from .predefined import latex_color_codes, latex_color_names
