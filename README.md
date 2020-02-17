# logo

**This package is not unit-tested and not intended for distribution with the PySAL-meta package.**

### Description
     * Create the PySAL logo with TeX/TikZ, then create favicons at specified resolutions with ImageTricks. The original logo design was based on Figure 1 from Rey and Anselin (2007). Examples are given within `create_logo()` and `create_favicon()`. Further examples can be found in `PySAL_logo_creation.ipynb`.
        * Rey, S. J. and Anselin, L. (2007). PySAL: A python library of
    spatial analytical methods. The Review of Regional Studies, 37(1):5–27.
    
### How to use
    * See the `Examples` sections of the `create_logo()` and
      `create_favicon()` docstrings.
    * See `PySAL_logo_creation.ipynb` for more examples.

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

### Note
    * The default font for generating the PySAL logo is set to `M+ 1mn`. Once the M+ fonts are downloaded (see Requirements above) the `M+ 1mn` font must be installed.

### Authors
    * Serge Rey,
    * Luc Anselin,
    * James Gaboardi <jgaboardi@gmail.com>,
    * Wei Kang,
    * Eli Knaap

### File creation date
    * 2019-12
