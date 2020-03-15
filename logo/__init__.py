__version__ = "0.0.2"
"""
:mod:`logo` --- logo generation for the PySAL project
=====================================================
"""
from .create_pysal_logo import create_logo, create_favicon

# main themes ------------------------------------------------------------------
from .predefined import CHILD_NODES, GRANDCHILD_NODES
from .predefined import NO_TEXT, GREEK, BULLETS
from .predefined import WHITE, BLACK, DARKGRAY, TRANSPARENT
from .predefined import traditional_theme_transparent
from .predefined import traditional_theme_light, traditional_theme_dark
from .predefined import canon2020_theme_transparent
from .predefined import canon2020_theme_light, canon2020_theme_dark
from .predefined import cb_qual_Paired_n7_theme_transparent
from .predefined import cb_qual_Paired_n7_theme_light, cb_qual_Paired_n7_theme_dark
from .predefined import cb_qual_Set1_n7_theme_transparent
from .predefined import cb_qual_Set1_n7_theme_light, cb_qual_Set1_n7_theme_dark
from .predefined import latex_color_codes, latex_color_names

# submodule themes -------------------------------------------------------------
from .predefined import spaghetti_theme_transparent

# navigation (text outside concept) logo text / syntax -------------------------
from .predefined import psnav_1line, psnav_2line
from .predefined import spgh_long