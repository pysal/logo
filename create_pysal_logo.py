"""
Description:
    Create the PySAL logo with TeX/TikZ, then create
    favicons at specified resolutions with ImageTricks.
    The original logo design was based on Figure 1 from Rey and Anselin (2007)
    and can be created by simply running `python create_pysal_logo.py` from
    the command line (assuming all requirements are installed). More detailed 
    examples are given within `create_pysal_logo()` and `create_favicon()`.
    Further examples can be found in `logo_palette.ipynb`.
    
    Rey, S. J. and Anselin, L. (2007). PySAL: A python library of
        spatial analytical methods. The Review of Regional Studies, 37(1):5–27.

Requirements:
    Python 3.6+ (numpy)
    LuaTeX, Version 1.10.0 (TeX Live 2019)
    M+ fonts
        info -- https://mplus-fonts.osdn.jp/about-en.html
        download -- https://osdn.net/projects/mplus-fonts/releases/<RELEASE>
            The files created with the initial push for this file were run
            on release <62344>. The current release for download is <p14454>.
    ImageTricks (for favicon creation)
        https://www.belightsoft.com/products/imagetricks/

Note 1:
    The default font for generating the PySAL logo is set to `M+ 1mn`.
    Once the M+ fonts are downloaded (see Requirements above) the 
    `M+ 1mn` font must be installed.

Note 2:
    Changing child colors can be done in `_7_NODE_COLORS`, but use
    caution as some colors don't blend well when combining schema as
    is done here. For example, instead of 'gray' for the root node
    color use 'rgb:black,1.25;white,1' (the default argument value for
    `concept_color` in `create_logo()`). Also, note that RBG colors
    do not (at the time of the writing) blend well with CMY colors.
    See the following:
    https://ipfs-sec.stackexchange.cloudflare-ipfs.com/tex/A/question/24434.html
    https://tex.stackexchange.com/questions/48662/tikz-or-xcolor-lighten-color
    https://tex.stackexchange.com/questions/308853/why-does-xcolor-lighten-a-color-when-mixed

Authors:
    Serge Rey,
    Luc Anselin,
    James Gaboardi <jgaboardi@gmail.com>,
    Wei Kang,
    Eli Knaap,
    others?

File creation date:
    2019-12
"""


import itertools
import numpy
import subprocess


__version__ = "0.0.1"


# Predefined file name
OUT_FILE = "pysal_logo"

# Predefined themes: node colors, and node text (if desired)
# 1. Mimic the original theme colors from Rey and Anselin (2007).
ORIG_COLORS = [
    "violet",
    "black!10!red",
    "blue",
    "black!50!green",
    "brown",
    "black!40!red",
    "orange",
]
ORIG_TEXT = [""] * len(ORIG_COLORS)
ORIGINAL_THEME = numpy.array(list(zip(ORIG_COLORS, ORIG_TEXT)))

# 2. Variation on (1.)
VARIATION_COLORS = [
    "cyan!16.666666666666668!magenta",
    "black!10!red",
    "blue",
    "black!50!green",
    "cyan!66.66666666666667!magenta",
    "black!40!red",
    "orange",
]
VARIATION_THEME = numpy.array(list(zip(VARIATION_COLORS, ORIG_TEXT)))

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


def check_for_cmy(node_info):
    """check for Cyan-Magenta-Yellow color schema"""
    # isolate selected colors/shades
    node_colors = node_info[:, 0]
    # initialize color schema as RGB
    CMY = {
        "cyan": False,
        "magenta": False,
        "yellow": False,
        "teal": False,
        "olive": False
    }
    # filter out all colors in logo
    color_elements = list(
        itertools.chain.from_iterable([c.split("!") for c in node_colors])
    )
    colors = set([c for c in color_elements if c.isalpha()])
    # hunt for any CMY colors
    for c in colors:
        if c in CMY:
            CMY[c] = True
    return CMY, colors


def set_header_and_footer(font, convert_tikz, cmy, colors):
    header = r"""
    \documentclass[tikz%s]{standalone}
    \usetikzlibrary{mindmap,trees}
    \usepackage{fontspec}
    \defaultfontfeatures{Ligatures=TeX,Scale=3}
    \setmainfont{%s}""" % (
        convert_tikz,
        font,
    )
    # adjust/declare colors as necessary
    if any(cmy.values()):
        for color in colors:
            header += r"""
            \colorlet{%s}[rgb]{%s}""" % (
                color,
                color,
            )
    header += r"""
    \begin{document}"""
    footer = r"""
    \end{document}"""
    return header, footer


def level_distances_and_sibling_angles(child_nodes, grandchild_nodes):
    """Alter this function for varying child/grandchild configurations."""
    if child_nodes == 7:
        dist_l1, angle_l1 = "5cm", "51"
    if grandchild_nodes == 3:
        dist_l2, angle_l2 = "3cm", "45"
    return dist_l1, angle_l1, dist_l2, angle_l2


def initialize_tikz(
    concept_color,
    text_color,
    level_distance_1,
    sibling_angle_1,
    level_distance_2,
    sibling_angle_2,
    font_size_l1="Huge",
):
    """
    see `level_distances_and_sibling_angles()` for adjusting the
    `level distance` and `sibling angle` parameters for the 
    tikzpicture mindmap/concept.
    """
    # pack distance, angle, and font arguments for each level
    args_l1 = level_distance_1, sibling_angle_1, font_size_l1
    args_l2 = level_distance_2, sibling_angle_2
    # initialize tikz picture
    main_content = r"""
    \begin{tikzpicture}[
        mindmap,
        grow cyclic,
        every node/.style=concept,
        concept color=%s,
        text=%s,
        level 1/.append style={
            level distance=%s,
            sibling angle=%s,
            font=\%s
        },
        level 2/.append style={
            level distance=%s,
            sibling angle=%s
        }
    ]
    """ % (
        concept_color,
        text_color,
        *args_l1,
        *args_l2,
    )
    return main_content


def finalize_tikz():
    end_tikzpicture = r"""
                ;
    \end{tikzpicture}"""
    return end_tikzpicture


def create_grandchild():
    # create a grandchild node
    grandchild = r"""
            child { node { }}"""
    return grandchild


def create_child(child_color, grandchildren, child_text):
    # create a child node
    child = r"""
        child [concept color=%s]{ node {%s}""" % (
        child_color,
        child_text,
    )
    # create grandchildren nodes for the child
    for grandchild in range(grandchildren):
        child += create_grandchild()
    # finalize child syntax
    child += r"""
         }"""
    return child


def create_root(concept_color, root_text, root_font_style, root_font_size):
    tikz_root = r"""
        \node[concept color=%s]{\%s\%s{%s}}""" % (
        concept_color,
        root_font_size,
        root_font_style,
        root_text,
    )
    return tikz_root


def create_logo(
    fname,
    node_info=None,
    concept_color=r"{rgb:black,1.25;white,1}",
    root_text="PySAL",
    text_color="white",
    root_font_style="bfseries",
    root_font_size="large",
    grandchild_nodes=3,
    font="M+ 1mn",
    engine="lualatex",
    convert_tikz=r",convert={outfile=\jobname.png}",
    clean_up=["aux", "log", "pdf"],
):
    """Create the PySAL logo with TeX/TikZ by initializing and 
    appending a raw text file before saving it out as a .tex file.
    Following the .tex file create, perform a command line call.
    
    Parameters
    ----------
    
    fname : str
        Logo file name.
    
    node_info : iterable (Optional - Default is None)
        List two zipped lists; one containing node color information
        and the other containing node text information. More information
        about node colors and blending can be found at the websites listed
        at the top of the file in the Note1 section.
    
    concept_color : str (Optional - Default is r"{rgb:black,1.25;white,1}")
        Root node (and transitions into children nodes) color.
    
    root_text : str (Optional - Default is "PySAL")
        Text within the root node.
    
    text_color : str (Optional - Default is "white")
        Text color within the root node.
    
    root_font_style : str (Optional - Default is "bfseries")
        Text font style within the root node.
    
    root_font_size : str (Optional - Default is "large")
        Text font size within the root node.
    
    grandchild_nodes : int (Optional - Default is 3)
        Number of grandchildren nodes for each child node.
    
    font : str (Optional - Default is "M+ 1mn")
        Font type. The font is
    
    engine : str (Optional - Default is "lualatex")
        TeX engine to compile to document.
    
    convert_tikz : str (Optional - Default is r",convert={outfile=\jobname.png})
        Automatically convert the resultant .pdf to a .png,
        in addition to the original .pdf. This parameter may also be set
        to .jpg, .svg, etc.
    
    clean_up : list (Optional - Default is ["aux", "log", "pdf"])
        Remove these types of files after processing. Add .tex to the
        list of the intermediary .text file is not needed following the
        create of the logo.
    
    Examples
    --------
    
    Create the standard PySAL logo based on the original design found in
    Rey and Anselin (2007).
    
    >>> from create_pysal_logo import create_logo, OUT_FILE, ORIGINAL_THEME
    >>> create_logo(OUT_FILE, ORIGINAL_THEME)
    
    Create the standard PySAL logo based on the original design found in
    Rey and Anselin (2007), but with Greek letter in the child nodes.
    
    >>> from create_pysal_logo import ORIG_COLORS, GREEK
    >>> greek_theme = numpy.array(list(zip(ORIG_COLORS, GREEK)))
    >>> create_logo(OUT_FILE, greek_theme)
    
    Create the PySAL logo with a customized color palette and no text.
    
    >>> from create_pysal_logo import VARIATION_THEME
    >>> create_logo(OUT_FILE, VARIATION_THEME)
    
    Create the PySAL logo with a customized color palette and customized text.
    
    >>> from create_pysal_logo import VARIATION_COLORS
    >>> text = [
    ...     r"$\bullet$", r"$S$", r"$A$", r"$L$", r"$\bullet$", r"$y$", r"$P$"
    ... ]
    >>> custom_theme = numpy.array(list(zip(VARIATION_COLORS, text)))
    >>> create_logo(OUT_FILE, custom_theme)
    
    Create a gradient blend of two colors.
    
    >>> from create_pysal_logo import ORIG_TEXT
    >>> alphas = numpy.linspace(0, 100, len(ORIG_TEXT))
    >>> gradient = ["blue!%s!cyan" % alpha for alpha in alphas]
    >>> custom_theme = numpy.array(list(zip(gradient, ORIG_TEXT)))
    >>> create_logo(OUT_FILE, custom_theme)
    
    """

    # check for Cyan-Magenta-Yellow color schema
    cmy, colors = check_for_cmy(node_info)

    # create the .tex header and footer
    tex_header, tex_footer = set_header_and_footer(font, convert_tikz, cmy, colors)

    # set number of child nodes based on number of colors
    child_nodes = len(node_info)

    # set level distances and sibling angles
    leveldistance_siblingangle = level_distances_and_sibling_angles(
        child_nodes, grandchild_nodes
    )

    # create the tikz preamble
    tex_content = initialize_tikz(
        concept_color, text_color, *leveldistance_siblingangle
    )

    # create the root node for the concept mindmap
    tex_content += create_root(
        concept_color, root_text, root_font_style, root_font_size
    )

    # create each child node (and grandchild node within)
    for color, text in node_info:
        tex_content += create_child(color, grandchild_nodes, text)

    # finalize the tikz object
    tex_content += finalize_tikz()

    # combine all .tex file content
    fcontent = tex_header + tex_content + tex_footer

    # write the .tex file
    with open("%s.tex" % fname, "w") as f:
        f.write(fcontent)

    # create the logo with a terminal call
    # see the following for reasoning:
    # https://tex.stackexchange.com/questions/99475/how-to-invoke-latex-with-the-shell-escape-flag-in-texstudio-former-texmakerx/99476#99476
    if convert_tikz != "":
        shell_escape = "--shell-escape"
    else:
        shell_escape = convert_tikz
    subprocess.Popen([engine, shell_escape, "%s.tex" % fname]).wait()

    # This works on OSX, may not work on other operating systems
    if clean_up:
        find = ["find", "-E", ".", "-type", "f", "-maxdepth", "1", "-regex"]
        find.extend([r".*\.(%s)" % "|".join(clean_up), "-delete"])
        subprocess.Popen(find).wait()


def create_favicon(
    fname, node_info=None, root_text="", resolutions=[32, 48, 64], clean_up=True
):
    """Create the PySAL logo favicon (.ico) files at desired resolutions.
    
    Parameters
    ----------
    
    fname : see `create_logo()`
    
    node_info : see `create_logo()`
    
    root_text : see `create_logo()`
    
    resolutions : list (Default is [32, 48, 64])
        Resolutions for the .ico files. Can include `[16, 28, 32, 48, 64]`.
    
    clean_up : bool (Default is True)
        Remove all files needed to create the .ico files.
    
    Examples
    --------
    
    Create the standard PySAL favicons based on the original design found in
    Rey and Anselin (2007) at the three default resolutions.
    
    >>> from create_pysal_logo import create_favicon, OUT_FILE, ORIGINAL_THEME
    >>> create_favicon(OUT_FILE, ORIGINAL_THEME)
    
    Create the standard PySAL favicons based on the original design found in
    Rey and Anselin (2007) at a single resolution.
    
    >>> create_favicon(OUT_FILE, ORIGINAL_THEME, resolutions=[64])
    
    """

    # set .ico file names
    favicon = "favicon"
    fname = "%s_%s" % (fname, favicon)

    # create a logo with no root text
    create_logo(fname, node_info=node_info, root_text=root_text)

    # create favicons
    for resolution in resolutions:
        subprocess.Popen(
            [
                "convert",
                "%s.png" % fname,
                "-background",
                "white",
                "-clone",
                "0",
                "-resize",
                "%sx%s" % (resolution, resolution),
                "-extent",
                "%sx%s" % (resolution, resolution),
                "-delete",
                "0",
                "-alpha",
                "off",
                "-colors",
                "256",
                "%s_%s.ico" % (fname, resolution),
            ]
        ).wait()

    # remove all files needed to create the favicons
    # except the favicons themselves
    if clean_up:
        find = ["find", ".", "-type", "f", "-maxdepth", "1", "-name"]
        find.extend(["%s.*" % fname, "-delete"])
        subprocess.Popen(find).wait()


if __name__ == "__main__":

    # Create the standard PySAL logo based on Rey and Anselin (2007).
    # create full logo
    create_logo(OUT_FILE, ORIGINAL_THEME)
     # create logo favicons
    create_favicon(OUT_FILE, ORIGINAL_THEME)
