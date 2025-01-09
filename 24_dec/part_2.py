import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from part_1 import (
    get_input,
    get_value
)

def print_diff(expected, state):
    as_bin = bin(expected)[2:]
    diff = ''.join('|' if val != state[i] else '-' for i, val in enumerate(as_bin))
    print(f"Exp:   {as_bin}\nDiff:  {diff}\nState: {''.join(state)}")


@timed
def main():
    state, operations = get_input('./input.txt')
    x_regs = sorted(filter(lambda reg: reg.startswith('x'), state.keys()), reverse=True)
    y_regs = sorted(filter(lambda reg: reg.startswith('y'), state.keys()), reverse=True)
    expected = int(''.join((str(state[x]) for x in x_regs)), base=2) + int(''.join((str(state[y]) for y in y_regs)), base=2)
    end_regs = sorted(filter(lambda reg: reg.startswith('z'), operations.keys()), reverse=True)
    end_state = [str(get_value(reg, state, operations)) for reg in end_regs]
    output_wires = operations.keys()
    print_diff(expected, end_state)

if __name__ == "__main__":
    main()
