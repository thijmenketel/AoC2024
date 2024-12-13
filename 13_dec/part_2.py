import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
import re
from part_1 import (
    get_input,
    get_solutions
)

TRILLIONEE = 10000000000000

def get_input(filename):
    with open(filename, 'r') as file:
        equations = []
        machines = file.read().strip().split('\n\n')
        for machine in machines:
            nums = [[int(x) for x in re.findall(r'\d+', line)] for line in machine.split('\n')]                
            a = (nums[0][0], nums[1][0], TRILLIONEE + nums[2][0])
            b = (nums[0][1], nums[1][1], TRILLIONEE + nums[2][1])
            equations.append((a, b))
        return equations

@timed
def main():
    equations = get_input('./input.txt')
    solutions = get_solutions(equations)
    print(int(sum([3*a + b for a, b in solutions])))

if __name__ == "__main__":
    main()
