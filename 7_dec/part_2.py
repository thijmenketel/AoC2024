import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from multiprocessing import Pool
from math import log10
from util import timer
from numpy import base_repr
from part_1 import (
    get_input,
    add, mul
)

# def concat(a, b): return int(f"{a}{b}")
def concat(a, b): return a * (10 ** (int(log10(b)) + 1)) + b

def get_option(vars, opt):
    order = list(reversed(base_repr(opt, base=3, padding=len(vars)-1)))
    ops = {'0': add, '1': mul, '2': concat}
    result = vars[0]
    for op, var in zip(order, vars[1:]):
        result = ops[op](result, var)
    return result

def is_correct_answer(line):
    answer, vars = line
    options = pow(3, len(vars)-1)
    for opt in range(options):
        if answer == get_option(vars, opt):
            return True
    return False

def main():
    data = get_input('./input.txt')
    with Pool(14) as p:
        filtered = p.map(is_correct_answer, data.items())
    print(sum([x[0] for x, keep in zip(data.items(), filtered) if keep]))

if __name__ == "__main__":
    with timer():
        main()
