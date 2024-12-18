import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from computer import Computer
from part_1 import (
    get_input
)

@timed
def main():
    registers, program = get_input('./input.txt')

    comp = Computer(registers)
    comp.reset()

    vals = [0]
    idx = 0
    while vals:
        if idx == len(program):
            print(min(vals))
            break
        exp = program[len(program)-idx-1:]
        for _ in range(len(vals)):
            t = vals.pop(0)
            for k in range(8):
                a_val = 8*t + k
                result = comp.run_program(program, a_val)
                if result == exp: vals.append(a_val)
                comp.reset()
        idx += 1


if __name__ == "__main__":
    main()
