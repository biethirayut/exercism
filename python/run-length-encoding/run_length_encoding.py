import re
from itertools import groupby


def decode(string):
    groups = re.findall('(\d*\D{1})', string)
    pairs = map(lambda g: [re.match('\d*', g).group(), g[-1]], groups)
    return ''.join(map(lambda x: int(x[0]) * x[1] if x[0].isdigit() else x[1],
                       pairs))


def encode(string):
    return ''.join(map(lambda g: helper(g), [list(g) for k, g in groupby(string)]))


def helper(g):
    return g[0] if len(g) == 1 else str(len(g)) + g[0]
