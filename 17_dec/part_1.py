import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from computer import Computer
import re

def get_input(filename):
    with open(filename, 'r') as file:
        register, program = file.read().strip().split('\n\n')
        register = [int(x) for x in re.findall(r'\d+', register)]
        program = [int(x) for x in re.findall(r'\d+', program)]
        return register, program

@timed
def main():
    registers, program = get_input('./input.txt')
    for i in range(1000):
        comp = Computer(registers)
        comp.run_program(program, i)

if __name__ == "__main__":
    main()
