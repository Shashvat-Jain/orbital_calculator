import math

"""
NAME - SHASHVAT JAIN 
ADMISSION NO. - 20JE0897
"""


def sc(z):
    if z > 0:
        return (1 - math.cos(math.sqrt(z))) / z
    if z < 0:
        return (math.cosh(math.sqrt(-z)) - 1) / (-z)
    else:
        return 1 / 2


def ss(z):
    if z > 0:
        return (math.sqrt(z) - math.sin(math.sqrt(z))) / (math.sqrt(z)) ** 3
    if z < 0:
        return (math.sinh(math.sqrt(-z)) - math.sqrt(-z)) / (math.sqrt(-z)) ** 3
    else:
        return 1 / 6


def main(m, x, t, r, ro, a):
    z = a * x * x
    f = 1 - (x * x / ro) * sc(z)
    g = t - (1 / math.sqrt(m)) * x * x * x * ss(z)
    fdot = (math.sqrt(m) / (r * ro)) * (z * ss(z) - 1) * x
    gdot = 1 - (x * x / r) * sc(z)
    return (f, g, fdot, gdot)
