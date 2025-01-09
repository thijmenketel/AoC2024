import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed

def get_input(filename):
    with open(filename, 'r') as file:
        state, operations = file.read().strip().split('\n\n')
        state = {reg: int(val) for reg, val in (line.split(': ') for line in state.split('\n'))}
        operations = {reg: ops for ops, reg in (line.split(' -> ') for line in operations.split('\n'))}
        return state, operations
    
def get_op(op):
    return {
        'AND': lambda x, y: x & y,
        'OR': lambda x, y: x | y,
        'XOR': lambda x, y: x ^ y,
    }[op]

def get_value(reg, state, ops):
    if reg in state: return state[reg]
    reg1, op, reg2 = ops[reg].split(' ')
    return get_op(op)(get_value(reg1, state, ops), get_value(reg2, state, ops))

@timed
def main():
    state, operations = get_input('./input.txt')
    end_regs = sorted(filter(lambda reg: reg.startswith('z'), operations.keys()), reverse=True)
    end_state = [str(get_value(reg, state, operations)) for reg in end_regs]
    print(int(''.join(end_state), base=2))

if __name__ == "__main__":
    main()
