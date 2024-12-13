import sys
import os

import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
import re

def get_input(filename):
    with open(filename, 'r') as file:
        equations = []
        machines = file.read().strip().split('\n\n')
        for machine in machines:
            nums = [[int(x) for x in re.findall(r'\d+', line)] for line in machine.split('\n')]                
            a = (nums[0][0], nums[1][0], nums[2][0])
            b = (nums[0][1], nums[1][1], nums[2][1])
            equations.append((a, b))
        return equations

def solve_for(a, b):
    coefficients = np.array([[a[0], a[1]],[b[0], b[1]]])
    constants = np.array([a[2], b[2]])
    # sol = np.linalg.inv(coefficients).dot(constants)
    sol = np.linalg.solve(coefficients, constants)
    return sol

def get_solutions(equations):
    return [sols for sols in [solve_for(a, b) for a, b in equations] if all(
        round(sol, 3) % 1 == 0
        for sol in sols
    )]

@timed
def main():
    equations = get_input('./input.txt')
    solutions = get_solutions(equations)
    print(int(sum([3*a + b for a, b in solutions])))

if __name__ == "__main__":
    main()
