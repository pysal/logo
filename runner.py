"""
For quick creation of the modernized 'canon2020/PySAL2020' logo
run the following from the command line within the top directory:

    $ python runner.py
    
"""

from logo import create_logo, create_favicon
from logo import canon2020_theme_transparent, psnav_1line, psnav_2line


# Create the default canon2020/PySAL2020 logo
# and favicons with a transparent background
logo_name = "pysal_logo"

# create the logo
create_logo(logo_name, **canon2020_theme_transparent)

# create favicons
fcon_res = ["32", "48", "64"]
canon2020_theme_transparent["concept_text"] = ""
for fr in fcon_res:
    create_favicon(logo_name, resolution=fr, **canon2020_theme_transparent)

# create the navigation/index logos
canon2020_theme_transparent["nav_logo"] = psnav_1line
create_logo("pysal_nav_logo_1line", fmat="svg", **canon2020_theme_transparent)
canon2020_theme_transparent["nav_logo"] = psnav_2line
create_logo("pysal_nav_logo_2line", fmat="svg", **canon2020_theme_transparent)