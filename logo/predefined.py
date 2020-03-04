"""Pre-defined elements for the creation of a PySAL logo.
    - text
    - ColorBrewer2 schemes (http://colorbrewer2.org)
    - LaTeX defined colors (http://latexcolor.com/)
    - tikz mindmap/concept colors, ans backgrounds, etc.
    - complete theme templates
"""

import numpy

from . import defined_latex_colors


def create_dict(_names, _codes, _format="RGB"):
    """Helper for ColorBrewer2"""
    schema = {}
    for i, (n, f, c) in enumerate(zip(_names, [_format] * len(_names), _codes)):
        schema[i] = {n: {f: c}}
        c = str([float(x) / 255.0 for x in c.split(",")])
        schema[i][n].update({f.lower(): {c}})
    return schema


def _theme_builder(theme_info, background):
    """Helper for building a theme."""
    # set the color names and codes for ColorBrewer2 defined colors
    if type(theme_info) == str:
        if theme_info == "cb_qual_Set1_n7":
            theme_colors = cb_qual_Set1_n7
        elif theme_info == "cb_qual_Paired_n7":
            theme_colors = cb_qual_Paired_n7
        elif theme_info == "canon2020":
            theme_colors = canon2020
        else:
            raise RuntimeError("'%s' theme not found." % theme_info)
        _theme_colors = []
        for idx, color_codes in theme_colors.items():
            color = list(color_codes.keys())[0]
            _theme_colors.append((idx, color, color_codes[color]["RGB"]))
        _theme_colors.sort()
        theme_colors = [tc[1:] for tc in _theme_colors]
    # set the color names and codes for LaTeX defined colors
    elif type(theme_info) == dict:
        theme_colors = [
            (idx, color, latex_color_codes[color]["RGB"])
            for idx, color in theme_info.items()
        ]
        theme_colors.sort()
        theme_colors = [tc[1:] for tc in theme_colors]
    else:
        raise RuntimeError("'%s' theme not in a recognized format." % theme_info)
    # combine color and text information for nodes
    node_info = numpy.array(list(zip(theme_colors, NO_TEXT)))
    # set background color
    if background == "light":
        background_color = WHITE
    else:
        background_color = BLACK
    # pack up theme information
    theme = {
        "node_info": node_info,
        "color_format": "RGB",
        "background_color": background_color,
        "concept_color": DARKGRAY,
        "text_color": WHITE,
    }
    return theme


################################################################################
#########################      PySAL Constants        ##########################
################################################################################

# The pysal logo should always have 7 children and 3 grandchildren per child
CHILD_NODES = 7
GRANDCHILD_NODES = 3


################################################################################
#########################      Pre-defined text        #########################
################################################################################

NO_TEXT = [""] * CHILD_NODES

# Greek lettering, including the PySAL W
GREEK = [
    r"$\theta$",
    r"$\gamma$",
    r"$\tau$",
    r"$\lambda$",
    r"$\alpha$",
    r"$W$",
    r"$\rho$",
]

# bullets
BULLETS = [r"$\bullet$"] * CHILD_NODES


################################################################################
################      ColorBrewer2 defined color schemes        ################
################################################################################
"""
Colors from http://colorbrewer2.org
Brewer, Cynthia A. ColorBrewer2. http://www.ColorBrewer.org, (2020-02).
"""
# based on http://colorbrewer2.org=qualitative&scheme=Paired&n=7
names = ["light blue", "dark blue", "light green", "dark green", "pink", "red", "beige"]
codes = [
    "166, 206, 227",
    "31, 120, 180",
    "178, 223, 138",
    "51, 160, 44",
    "251, 154, 153",
    "227, 26, 28",
    "253, 191, 111",
]
cb_qual_Paired_n7 = create_dict(names, codes)

# based on http://colorbrewer2.org=qualitative&scheme=Set1&n=7
names = ["red", "blue", "green", "purple", "orange", "yellow", "brown"]
codes = [
    "228, 26, 28",
    "55, 126, 184",
    "77, 175, 74",
    "152, 78, 163",
    "255, 127, 0",
    "255, 255, 51",
    "166, 86, 40",
]
cb_qual_Set1_n7 = create_dict(names, codes)


################################################################################
########################      LaTeX defined colors        ######################
################################################################################
"""
Based on `LatexColors.incl.tex` from 
            Dave Doolin -   http://latexcolor.com/
            Gilu -          http://latexcolor.com/#comment-4080334272
See also:   https://github.com/Inventium/latexcolor.com
            https://drive.google.com/drive/folders/1l_vDhUO6wfbj2DSBytEYD4AfNfwRJ5je
"""

latex_color_codes = defined_latex_colors.all_latex_colors
latex_color_names = defined_latex_colors.latex_color_names


################################################################################
############      Pre-defined concept colors and backgrounds        ############
################################################################################

WHITE = "white", latex_color_codes["white"]["RGB"]
BLACK = "black", latex_color_codes["black"]["RGB"]
DARKGRAY = "dimgray", latex_color_codes["dimgray"]["RGB"]


################################################################################
####################      Pre-defined theme templates        ###################
################################################################################

# these are indexed counterclockwise starting from ~8:00
# "Traditional" PySAL colors from Rey and Anselin (2007)
traditional_colors = {
    0: "byzantium",
    1: "alizarin",
    2: "blue",
    3: "green(html/cssgreen)",
    4: "frenchbeige",
    5: "darkred",
    6: "orange(colorwheel)",
}
# Tradition/Canonical PySAL themes ---------------------------------------------
traditional_theme_light = _theme_builder(traditional_colors, "light")
traditional_theme_dark = _theme_builder(traditional_colors, "dark")

# Canonical colors as of 02/2020 -----------------------------------------------
names = ["metallic", "tc", "yellow", "shamrock", "nvy", "vio", "orng"]
codes = [
    "0, 121, 140",
    "209, 73, 91",
    "237, 174, 73",
    "102, 161, 130",
    "46, 64, 87",
    "156, 100, 123",
    "239, 138, 23",
]
canon2020 = create_dict(names, codes)
canon2020_theme_light = _theme_builder("canon2020", "light")
canon2020_theme_dark = _theme_builder("canon2020", "dark")


# ColorBrewer2 themes ----------------------------------------------------------
cb_qual_Paired_n7_theme_light = _theme_builder("cb_qual_Paired_n7", "light")
cb_qual_Paired_n7_theme_dark = _theme_builder("cb_qual_Paired_n7", "dark")
cb_qual_Set1_n7_theme_light = _theme_builder("cb_qual_Set1_n7", "light")
cb_qual_Set1_n7_theme_dark = _theme_builder("cb_qual_Set1_n7", "dark")
