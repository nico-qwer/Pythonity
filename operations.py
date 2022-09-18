from itertools import product
from math import prod


def add_tuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

def multiply_tuple(tuple1, number, intify = False):
    product = (tuple1[0] * number, tuple1[1] * number)

    if intify == True:
        return (int(product[0]), int(product[1]))
    else:
        return product

def multiply_tuples(tuple1, tuple2, intify = False):
    product = (tuple1[0] * tuple2[0], tuple1[1] * tuple2[1])

    if intify == True:
        return (int(product[0]), int(product[1]))
    else:
        return product