"""

Description:
    Create the PySAL logo with TeX/TikZ, then create
    favicons at specified resolutions with ImageTricks.
    The original logo design was based on Figure 1 from Rey and Anselin (2007).
    Examples are given within `create_logo()` and `create_favicon()`.
    Further examples can be found in `PySAL_logo_creation.ipynb`.
    
    Rey, S. J. and Anselin, L. (2007). PySAL: A python library of
        spatial analytical methods. The Review of Regional Studies, 37(1):5–27.

How to use:
    1. See the `Examples` sections of the `create_logo()` and
        `create_favicon()` docstrings.
    2. See `PySAL_logo_creation.ipynb` for more examples.
    3. For quick creation of the modernized 'canon2020/PySAL2020' logo
        run the following from the command line within the top directory:
        
        $ python runner.py

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

Note:
    The default font for generating the PySAL logo is set to `M+ 1mn`.
    Once the M+ fonts are downloaded (see Requirements above) the 
    `M+ 1mn` font must be installed.

Authors:
    Serge Rey,
    Luc Anselin,
    James Gaboardi <jgaboardi@gmail.com>,
    Wei Kang,
    Eli Knaap

File creation date:
    2019-12

"""

import os
import subprocess

from .predefined import CHILD_NODES, GRANDCHILD_NODES
from . import build_tex_file


def create_logo(
    fname,
    node_info=None,
    color_format=None,
    background_color=None,
    concept_color=None,
    text_color=None,
    move_to=None,
    nav_logo=None,
    concept_text="PySAL",
    concept_font_style="bfseries",
    concept_font_size="large",
    font="M+ 1mn",
    engine="lualatex",
    convert_tikz=r",convert={outfile=\jobname.%s}",
    fmat="png",
    clean_up=["aux", "log", "pdf"],
):
    """
    
    Create the PySAL logo with TeX/TikZ by initializing and 
    appending a raw text file before saving it out as a .tex file.
    Following the .tex file creation, perform a command line call.
    
    Parameters
    ----------
    
    fname : str
        Logo file name.
    
    node_info : numpy.array
        A 7x2 array where each row represent the information for
        one child node. The first column of the array is a 2 element
        tuple in the form ("color name", "r, g, b"), where "r, g, b"
        are the specific RBG color values. The second column is the 
        node text.
    
    color_format : str
        Color system. 'RGB' appears to be the most robust.
    
    background_color :  tuple
        Logo background color. Tuple of (color name, color code).
    
    concept_color : tuple
        Color within the concept (root) node. Tuple of (color name, color code).
        This color transitions into children nodes' color.
    
    text_color : tuple
        Text color within the root node. Tuple of (color name, color code).
    
    move_to : str
        Default is None. Move the output to the directory.
    
    nav_logo : dict
        Parameters, including `text` and `font_style`, for creating the
        navigation logo found in `http://pysal.org/index.html`.
    
    concept_text : str (Optional - Default is "PySAL")
        Text within the root node.
    
    concept_font_style : str (Optional - Default is "bfseries")
        Text font style within the root node.
    
    concept_font_size : str (Optional - Default is "large")
        Text font size within the root node.
    
    font : str (Optional - Default is "M+ 1mn")
        Font type. The font is
    
    engine : str (Optional - Default is "lualatex")
        TeX engine to compile to document.
    
    convert_tikz : str (Optional - Default is r",convert={outfile=\jobname.%s})
        TiKz keywords for automatically converting the resultant .pdf
        to another format. See `fmat` below.
    
    fmat : str (Optional - png)
        Convert the resultant .pdf to this format.
        This parameter may also be set to .jpg, .svg, etc.
    
    clean_up : list (Optional - Default is ["aux", "log", "pdf"])
        Remove these types of files after processing. Add .tex to the
        list of the intermediary .text file is not needed following the
        create of the logo.
    
    Examples
    --------
    
    Create the standard PySAL logo based on the original design found in
    Rey and Anselin (2007).
    
    >>> import logo
    >>> file_name, theme = "pysal_logo", logo.traditional_theme_transparent
    >>> logo.create_logo(file_name, **theme)
    
    See `PySAL_logo_creation.ipynb` for more examples.
    
    """

    if len(node_info) != CHILD_NODES:
        err_msg = "There must be 7 elements in the logo, %s were passed in."
        raise RuntimeError(err_msg % len(node_info))

    non_node_colors = []
    for nnc in [background_color, concept_color, text_color]:
        if nnc:
            non_node_colors.append(nnc)

    defined_colors = list(node_info[:, 0]) + non_node_colors
    # remove `None`s
    defined_colors = [dc for dc in defined_colors if dc[0] != None and dc[1] != None]

    # create the .tex header and footer
    tex_header, tex_footer = build_tex_file.set_header_and_footer(
        font, convert_tikz % fmat, defined_colors, color_format
    )

    # set level distances and sibling angles
    leveldistance_siblingangle = build_tex_file.level_distances_and_sibling_angles(
        CHILD_NODES, GRANDCHILD_NODES
    )

    # create the tikz preamble
    tex_content = build_tex_file.initialize_tikz(
        nav_logo,
        background_color[0],
        concept_color[0],
        text_color[0],
        *leveldistance_siblingangle
    )

    # create the root node for the concept mindmap
    tex_content += build_tex_file.create_concept(
        concept_color[0], concept_text, concept_font_style, concept_font_size
    )

    # create each child node (and grandchild node within)
    for color, text in node_info:
        tex_content += build_tex_file.create_child(color[0], GRANDCHILD_NODES, text)

    # finalize the tikz object
    tex_content += build_tex_file.finalize_tikz(nav_logo)

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

    # move the products to a new directory
    if move_to:
        currdir = os.getcwd()
        fs = [f for f in os.listdir(currdir) if f.startswith("%s" % fname)]
        [os.rename(f, "%s/%s%s" % (currdir, move_to, f)) for f in fs]


def create_favicon(
    fname,
    node_info=None,
    color_format=None,
    background_color=None,
    concept_color=None,
    text_color=None,
    move_to=None,
    concept_text=None,
    resolutions="64,48,32,16",
    clean_up=True,
):
    """
    
    Create a PySAL logo favicon (.ico) file at the desired resolution.
    
    Parameters
    ----------
    
    fname : see `create_logo()`
    
    node_info : see `create_logo()`
    
    background_color : see `create_logo()`
    
    move_to : see `create_logo()`
    
    concept_text : see `create_logo()`
    
    color_format : see `create_logo()`
    
    resolutions : str (Default is '64,48,32,16')
        Auto-resize to these resolutions for the .ico files.
    
    clean_up : bool (Default is True)
        Remove all files needed to create the .ico files.
    
    Examples
    --------
    
    Create the standard PySAL favicons based on the original design found in
    Rey and Anselin (2007) at a resolution of 32x32.
    
    >>> import logo
    >>> file_name, theme = "pysal_logo", logo.traditional_theme_transparent
    >>> theme["concept_text"] = ""
    >>> logo.create_favicon(file_name, **theme)
    
    """

    # set .ico file names
    favicon = "favicon"
    fname = "%s_%s" % (fname, favicon)

    # create a logo with no root text
    create_logo(
        fname,
        node_info=node_info,
        color_format=color_format,
        background_color=background_color,
        concept_color=concept_color,
        concept_text=concept_text,
        text_color=text_color,
        move_to=move_to,
    )

    # create favicons
    subprocess.Popen(
        [
            "convert",
            "%s.png" % fname,
            "-define",
            "icon:auto-resize=%s" % resolutions,
            "%s.ico" % fname,
        ]
    ).wait()

    # remove all files needed to create the favicons
    # except the favicons themselves
    if clean_up:
        find = ["find", ".", "-type", "f", "-maxdepth", "1"]
        find.extend(["-name", "%s.*" % fname])
        find.extend(["!", "-name", "%s.ico" % fname])
        find.extend(["-delete"])
        subprocess.Popen(find).wait()

    # move the products to a new directory
    if move_to:
        currdir = os.getcwd()
        fs = [f for f in os.listdir(currdir) if f.startswith("%s" % fname)]
        [os.rename(f, "%s/%s%s" % (currdir, move_to, f)) for f in fs]
