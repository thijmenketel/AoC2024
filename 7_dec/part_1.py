import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timer

def get_input(filename):
    with open(filename, 'r') as file:
        data = {}
        for line in file:
            answer, vars = line.split(':')
            data[int(answer)] = list(map(int, vars.strip().split(' ')))
    return data

def add(a,b): return a + b
def mul(a,b): return a * b

def get_option(vars, opt):
    order = list(reversed(bin(opt)[2:].zfill(len(vars)-1)))
    ops = {'0': add, '1': mul}
    result = vars[0]
    for op, var in zip(order, vars[1:]):
        result = ops[op](result, var)
    return result

def is_correct_answer(line):
    answer, vars = line
    options = pow(2, len(vars)-1)
    for opt in range(options):
        option = get_option(vars, opt)
        if option == answer:
            return True
    return False

def main():
    data = get_input('./input.txt')
    print(sum(map(lambda d: d[0], filter(is_correct_answer, data.items()))))

if __name__ == "__main__":
    with timer():
        main()
