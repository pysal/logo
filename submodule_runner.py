"""
For quick creation of the spaghetti logo
run the following from the command line within the top directory:

    $ python submodule_runner.py
    
"""

from logo import create_logo
from logo import spaghetti_theme_transparent, spgh_long

# Create the default canon2020/PySAL2020 logo
# and favicons with a transparent background
spaghetti_theme_transparent.update({"move_to":"./submodule_examples/"})
logo_name = "spaghetti_logo"

# create the logo
create_logo(logo_name, **spaghetti_theme_transparent)

# create the navigation/index logo
spaghetti_theme_transparent["concept_text"] = ""
spaghetti_theme_transparent["nav_logo"] = spgh_long
create_logo("spaghetti_nav_logo", fmat="svg", **spaghetti_theme_transparent)