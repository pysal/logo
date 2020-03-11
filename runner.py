"""
For quick creation of the modernized 'canon2020/PySAL2020' logo
run the following from the command line within the top directory:

    $ python runner.py
    
"""

from logo import create_logo, create_favicon, canon2020_theme_transparent

# Create the default canon2020/PySAL2020 logo
# and favicons with a transparent background

canon2020_theme_transparent.update({"move_to":None})
base_name = "pysal_logo"
logo_name = base_name

# create the logo
create_logo(logo_name, **canon2020_theme_transparent)

# create favicons
fcon_res = ["32", "48", "64"]
canon2020_theme_transparent["concept_text"] = ""
for fr in fcon_res:
    create_favicon(base_name, resolution=fr, **canon2020_theme_transparent)
