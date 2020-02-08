# logo

### Description
 * Create the PySAL logo with TeX/TikZ, then create
    favicons at specified resolutions with ImageTricks.
    The original logo design was based on Figure 1 from Rey and Anselin (2007)
    and can be created by simply running `python create_pysal_logo.py` from
    the command line (assuming all requirements are installed). More detailed 
    examples are given within 
    [`create_pysal_logo()`](https://github.com/pysal/logo/blob/f028534c31622beeea295418b1e0e5a37e3413b4/create_pysal_logo.py#L270) 
    and [`create_favicon()`](https://github.com/pysal/logo/blob/f028534c31622beeea295418b1e0e5a37e3413b4/create_pysal_logo.py#L428).
    Further examples can be found in [`logo_palette.ipynb`](https://github.com/pysal/logo/blob/master/logo_palette.ipynb).
    
    * Rey, S. J. and Anselin, L. (2007). PySAL: A python library of
    spatial analytical methods. The Review of Regional Studies, 37(1):5–27.
    
### How to use
  * From the command line
        
    ```
    $ python create_pysal_logo.py
    ```

    The call above will produce a logo & favicons with colors 
    reminiscent of the original logo in Rey and Anselin (2007)
    and without text the child nodes.

    ```
    $ python create_pysal_logo.py red,blue,red,blue,red,blue,red
    ```

    The call above will produce a logo & favicons with alternating
    red and blue child nodes, without text inside the child nodes.

    ```
    $ python create_pysal_logo.py red,red,red,red,red,red,red 1,1,1,1,1,1,1
    ```

    The call above will produce a logo & favicons with all
    red child nodes, and a "1" inside each of the child nodes.
    
  * See logo_palette.ipynb for more examples.

### Requirements
  * Python 3.6+ (numpy)
  * LuaTeX, Version 1.10.0 (TeX Live 2019)
  * M+ fonts
      * info -- https://mplus-fonts.osdn.jp/about-en.html
      * download -- https://osdn.net/projects/mplus-fonts/releases/<RELEASE>
        * The files created with the initial push for this file were run
          on release <62344>. The current release for download is <p14454>.
  * ImageTricks (for favicon creation)
      * https://www.belightsoft.com/products/imagetricks/

### Note 1
  * The default font for generating the PySAL logo is set to `M+ 1mn`.
  Once the M+ fonts are downloaded (see Requirements above) the 
  `M+ 1mn` font must be installed.

### Note 2
  * Changing child colors can be done in `_7_NODE_COLORS`, but use
  caution as some colors don't blend well when combining schema as
  is done here. For example, instead of 'gray' for the root node
  color use 'rgb:black,1.25;white,1' (the default argument value for
  `concept_color` in `create_logo()`). Also, note that RBG colors
  do not (at the time of the writing) blend well with CMY colors.
  * See the following
    * https://ipfs-sec.stackexchange.cloudflare-ipfs.com/tex/A/question/24434.html
    * https://tex.stackexchange.com/questions/48662/tikz-or-xcolor-lighten-color
    * https://tex.stackexchange.com/questions/308853/why-does-xcolor-lighten-a-color-when-mixed

### Authors
  * Serge Rey,
  * Luc Anselin,
  * James Gaboardi <jgaboardi@gmail.com>,
  * Wei Kang,
  * Eli Knaap

### File creation date
  * 2019-12
