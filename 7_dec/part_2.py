import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from multiprocessing import Pool
from math import log10
from util import timed
from part_1 import (
    get_input,
    add, mul
)

def concat(a, b): return a * (10 ** (int(log10(b)) + 1)) + b

def check_answer(answer, partial, vars):
    if not vars:
        return answer == partial
    for op in [mul, add, concat]:
        if check_answer(answer, op(partial, vars[0]), vars[1:]):
            return True
    return False

def is_correct_answer(line):
    answer, vars = line
    return check_answer(answer, vars[0], vars[1:])

@timed
def main():
    data = get_input('./input.txt')
    with Pool(14) as p:
        filtered = p.map(is_correct_answer, data.items())
    print(sum([x[0] for x, keep in zip(data.items(), filtered) if keep]))

if __name__ == "__main__":
    main()
