import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed

def get_input(filename):
    with open(filename, 'r') as file:
        return [line for line in file.read().strip().split('\n')]

def get_key(key):
    return {
        '7': (0, 0), '8': (1, 0), '9': (2, 0),
        '4': (0, 1), '5': (1, 1), '6': (2, 1),
        '1': (0, 2), '2': (1, 2), '3': (2, 2),
                     '0': (1, 3), 'A': (2, 3),
    }[key]

def get_dir(dir):
    return {
                     '^': (1, 0), 'A': (2, 0),
        '<': (0, 1), 'v': (1, 1), '>': (2, 1),
    }[dir]

def get_movement(start, end):
     sx, sy = start
     ex, ey = end
     return (ex - sx), (ey - sy)

def get_sub_seq(dx, dy):
    seq = ''
    # move left first
    if dx < 0: seq += '<' * abs(dx)
    # move up/down
    if dy < 0: seq += '^' * abs(dy)
    if dy > 0: seq += 'v' * abs(dy)
    # move right
    if dx > 0: seq += '>' * abs(dx)
    seq += 'A'
    return seq

def get_dirs_for_code(code):
    curr, seq = 'A', ''
    for dig in code:
        c = get_key(curr)
        dx, dy = get_movement(c, get_key(dig))
        if (c[0], c[1] + dy) == (0, 3):
            # move right first
            if dx > 0: seq += '>' * abs(dx)
            dx = 0
        if (c[0] + dx, c[1]) == (0, 3):
            # move up first
            if dy < 0: seq += '^' * abs(dy)
            dy = 0
        seq += get_sub_seq(dx, dy)
        curr = dig
    return seq

def get_dirs_for_dirs(movements):
    curr, seq = 'A', ''
    for mov in movements:
        c = get_dir(curr)
        dx, dy = get_movement(c, get_dir(mov))
        if (c[0], c[1] + dy) == (0, 0):
            # move right first
            if dx > 0: seq += '>' * abs(dx)
            dx = 0
        if (c[0] + dx, c[1]) == (0, 0):
            # move down first
            if dy > 0: seq += 'v' * abs(dy)
            dy = 0
        seq += get_sub_seq(dx, dy)
        curr = mov
    return seq

@timed
def main():
    codes = get_input('./input.txt')
    complexity = 0
    for code in codes:
        dirs1 = get_dirs_for_code(code)
        dirs2 = get_dirs_for_dirs(dirs1)
        dirs3 = get_dirs_for_dirs(dirs2)
        print(f"{len(dirs3)} - {int(code.strip('A'))} \t{dirs3}")
        complexity += len(dirs3) * int(code.strip('A'))
    print(complexity)
if __name__ == "__main__":
    main()
