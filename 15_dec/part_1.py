import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from itertools import product

def get_input(filename):
    with open(filename, 'r') as file:
        grid, moves = file.read().strip().split('\n\n')
        grid = [[x for x in line] for line in grid.split('\n')]
        moves = [x for line in moves.split('\n') for x in line ]
    return grid, moves

def print_grid(grid, walls, boxes, robot):
    size = len(grid)
    grid = [['.' for _ in range(size)] for _ in range(size)]
    for y, x in product(range(size), range(size)):
        if (x, y) in walls:
            grid[y][x] = '#'
        elif (x, y) in boxes:
            grid[y][x] = 'O'
        elif (x, y) == robot:
            grid[y][x] = '@'
    for row in grid:
        print(''.join(row))
    print('-' * size)


def get_next_pos(pos, dir):
    x, y = pos
    match dir:
        case '^': return x, y-1
        case '>': return x+1, y
        case '<': return x-1, y
        case 'v': return x, y+1

def get_obstacles(grid):
    size = len(grid)
    walls, boxes = set(), set()
    for y, x in product(range(size), range(size)):
        match grid[y][x]:
            case '#': walls.add((x, y))
            case 'O': boxes.add((x, y))
    return walls, boxes

def move_box(box, dir, walls, boxes):
    n_pos = box
    while box in boxes:
        n_pos = get_next_pos(n_pos, dir)
        if n_pos in walls:
            return False
        if n_pos not in boxes:
            boxes.remove(box)
            boxes.add(n_pos)
    return True
        
@timed
def main():
    grid, moves = get_input('./input.txt')
    robot = ((len(grid)-1)//2, (len(grid)-1)//2)
    walls, boxes = get_obstacles(grid)
    print_grid(grid, walls, boxes, robot)
    for move in moves:
        n_pos = get_next_pos(robot, move)
        if n_pos in walls:
            continue
        if n_pos in boxes:
            if move_box(n_pos, move, walls, boxes):
                robot = n_pos
            else:
                continue
        robot = n_pos
    print_grid(grid, walls, boxes, robot)
    gps_sum = sum(list(map(lambda pos: 100*pos[1] + pos[0], boxes)))
    print(gps_sum)

if __name__ == "__main__":
    main()
