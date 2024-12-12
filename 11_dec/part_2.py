import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from functools import cache
from part_1 import (
    get_input,
    get_num_of_digits
)

def process_number(num, count, cache):
    if count == 0: return 1
    if (num, count) in cache: return cache[(num, count)]
    if num == 0: return process_number(1, count-1, cache)
    length = get_num_of_digits(num)
    if length % 2 == 0:
        a, b = divmod(num, 10 ** (length // 2))
        size = process_number(a, count-1, cache) + process_number(b, count-1, cache)
        cache[(num, count)] = size
        return size
    return process_number(num * 2024, count-1, cache)

@cache
def process_number2(num, count):
    if count == 0: return 1
    if num == 0: return process_number2(1, count-1)
    length = get_num_of_digits(num)
    if length % 2 == 0:
        a, b = divmod(num, 10 ** (length // 2))
        return process_number2(a, count-1) + process_number2(b, count-1)
    return process_number2(num * 2024, count-1)

@timed
def main():
    data = get_input('./input.txt')
    cache = dict()
    print(sum(map(lambda num: process_number(num, 75, cache), data)))
    # print(sum(map(lambda num: process_number2(num, 75), data)))

if __name__ == "__main__":
    main()
