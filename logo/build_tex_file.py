"""Functions for building the .tex file
"""

from .predefined import psnav_1line, psnav_2line


def set_header_and_footer(font, convert_tikz, colors, cformat):
    header = r"""
    \documentclass[tikz%s]{standalone}
    \usetikzlibrary{mindmap,trees,backgrounds}
    \usepackage{fontspec}
    \usepackage{lmodern}
    \defaultfontfeatures{Ligatures=TeX,Scale=3}
    \setmainfont{%s}
    
    """ % (
        convert_tikz,
        font,
    )

    defined = set()

    for color, code in colors:
        if color not in defined:
            header += r"""
    \definecolor{%s}{%s}{%s}""" % (
                color,
                cformat,
                code,
            )
            defined.add(color)

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
    nav_logo,
    background_color,
    concept_color,
    text_color,
    level_distance_1,
    sibling_angle_1,
    level_distance_2,
    sibling_angle_2,
    font_size_l1="Huge",
):
    """ see `level_distances_and_sibling_angles()` for adjusting the
    `level distance` and `sibling angle` parameters for the 
    tikzpicture mindmap/concept.
    """
    # pack distance, angle, and font arguments for each level
    args_l1 = level_distance_1, sibling_angle_1, font_size_l1
    args_l2 = level_distance_2, sibling_angle_2
    
    # set a scope environment if for the navigation/index logo
    if nav_logo:
        scope = r"""
        \begin{scope}"""
    else:
        scope = ""
    
    # set background of desired
    if background_color != None:
        background = r"""
        background rectangle/.style={fill=%s},
        show background rectangle,""" % background_color
    else:
        background = ""
    
    # initialize tikz picture
    main_content = r"""
    \begin{tikzpicture}%s[%s
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
        scope,
        background,
        concept_color,
        text_color,
        *args_l1,
        *args_l2,
    )
    return main_content


def finalize_tikz(nav_logo):
    # set scope variables if navigation logo
    if nav_logo:
        scope = r"""
        \end{scope}
        \begin{scope}
        %s
        \end{scope}""" % nav_logo
    else:
        scope = ""
    
    # final `tikzpicture` environment
    end_tikzpicture = r"""
                ;
    %s
    \end{tikzpicture}""" % scope
    
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


def create_concept(concept_color, concept_text, concept_font_style, concept_font_size):
    tikz_concept = r"""
        \node[concept color=%s]{\%s\%s{%s}}""" % (
        concept_color,
        concept_font_size,
        concept_font_style,
        concept_text,
    )
    return tikz_concept
