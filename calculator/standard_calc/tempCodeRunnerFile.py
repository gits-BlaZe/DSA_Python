import math
def band(x, y):
    return int(x) & int(y)
def bor(x, y):
    return int(x) | int(y)
def bxor(x, y):
    return int(x) ^ int(y)
def bnot(x):
    return ~int(x)
def lshift(x, positions=2):
    return int(x) << positions
def rshift(x, positions=2):
    return int(x) >> positions
def binary(x):
    bina= bin(int(x))
    return str((bina)[3:])
def octal(x):
    octa= oct(int(x))
    return str((octa)[3:])
def hexadecimal(x):
    hexa= hex(int(x))
    return str((hexa)[3:])
def btodecimal(x):
    return int(x, 2)
def otodecimal(x):
    return int(x, 8)
def htodecimal(x):
    return int(x, 16)