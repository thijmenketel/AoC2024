import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from operator import mul, add

def get_input(filename):
    with open(filename, 'r') as file:
        data = {}
        for line in file:
            answer, vars = line.split(':')
            data[int(answer)] = list(map(int, vars.strip().split(' ')))
    return data

def check_answer(answer, partial, vars):
    if not vars:
        return answer == partial
    for op in [mul, add]:
        if check_answer(answer, op(partial, vars[0]), vars[1:]):
            return True
    return False

def is_correct_answer(line):
    answer, vars = line
    return check_answer(answer, vars[0], vars[1:])

@timed
def main():
    data = get_input('./input.txt')
    print(sum(map(lambda d: d[0], filter(is_correct_answer, data.items()))))

if __name__ == "__main__":
    main()
