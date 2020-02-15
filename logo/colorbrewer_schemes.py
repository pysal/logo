"""Colors from http://colorbrewer2.org

Brewer, Cynthia A. ColorBrewer2. http://www.ColorBrewer.org, (2020-02).

"""


def create_dict(_names, _codes, _format="RGB"):
    schema = {}
    for n, f, c in zip(_names, [_format] * len(_names), _codes):
        schema[n] = {f: c}
        c = str([float(x) / 255.0 for x in c.split(",")])
        schema[n][_format.lower()] = c
    return schema


# ---------------------------------------------------------------
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

# ---------------------------------------------------------------
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
