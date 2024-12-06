import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timer

def get_input(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file if line]
    return grid

def find_guard(grid):
    for i, row in enumerate(grid):
        pos = ''.join(row).find('^')
        if pos != -1: return i, pos

def is_pos_in_grid(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

def next_pos(pos, dir):
    match dir:
        case '^': return pos[0]-1, pos[1]
        case '>': return pos[0], pos[1]+1
        case '<': return pos[0], pos[1]-1
        case 'v': return pos[0]+1, pos[1]

def turn_right(dir):
    match dir:
        case '^': return '>'
        case '>': return 'v'
        case 'v': return '<'
        case '<': return '^'

def traverse_grid(grid):
    dir = '^'
    pos = find_guard(grid)
    steps = [(dir, pos)]
    grid[pos[0]][pos[1]] = 'X'
    n_pos = next_pos(pos, dir)
    while is_pos_in_grid(grid, n_pos):
        match grid[n_pos[0]][n_pos[1]]:
            case '.':
                steps += [(dir, n_pos)]
                grid[n_pos[0]][n_pos[1]] = 'X'
                pos = n_pos
            case 'X': 
                pos = n_pos
            case '#': 
                dir = turn_right(dir)
        n_pos = next_pos(pos, dir)
    
    return steps

def main():
    grid = get_input('./test_input.txt')
    print(len(traverse_grid(grid)))
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    with timer():
        main()