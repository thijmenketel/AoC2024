import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from itertools import product
from part_1 import (
    get_input
)

def print_grid(grid, walls, l_boxes, r_boxes, robot):
    size = len(grid)
    grid = [['.' for _ in range(size*2)] for _ in range(size)]
    for y, x in product(range(size), range(size*2)):
        if (x, y) in walls:
            grid[y][x] = '#'
        elif (x, y) in l_boxes:
            grid[y][x] = '['
        elif (x, y) in r_boxes:
            grid[y][x] = ']'
        elif (x, y) == robot:
            grid[y][x] = '@'
    for row in grid:
        print(''.join(row))
    print('-' * size)


def get_next_pos(pos, dir, steps=1):
    x, y = pos
    match dir:
        case '^': return x, y-steps
        case '>': return x+steps, y
        case '<': return x-steps, y
        case 'v': return x, y+steps

def get_obstacles(grid):
    size = len(grid)
    walls, l_boxes, r_boxes = set(), set(), set()
    for y, x in product(range(size), range(size)):
        match grid[y][x]:
            case '#': 
                walls.add((x*2, y))
                walls.add((x*2+1, y))
            case 'O': 
                l_boxes.add((x*2, y))
                r_boxes.add((x*2+1, y))
    return walls, l_boxes, r_boxes

def move_box(box, dir, walls, l_boxes, r_boxes):
    x, y = box
    l_box = box if box in l_boxes else (x-1, y)
    r_box = box if box in r_boxes else (x+1, y)
    match dir:
        case '^': return move_ver('^', (l_box, r_box), walls, l_boxes, r_boxes)
        case 'v': return move_ver('v', (l_box, r_box), walls, l_boxes, r_boxes)
        case '<': return move_left((l_box, r_box), walls, l_boxes, r_boxes)
        case '>': return move_right((l_box, r_box), walls, l_boxes, r_boxes)
        
def move_left(box, walls, l_boxes, r_boxes):
    l, r = box
    n_pos = l
    while r in r_boxes:
        n_pos = get_next_pos(n_pos, '<')
        if n_pos in walls:
            return False
        if n_pos not in (l_boxes | r_boxes):
            to_move = r
            while to_move != n_pos:
                r_boxes.remove(to_move)
                left = get_next_pos(to_move, '<')
                r_boxes.add(left)
                l_boxes.remove(left)
                l_boxes.add(get_next_pos(left, '<'))
                to_move = get_next_pos(to_move, '<', 2)
    return True

def move_right(box, walls, l_boxes, r_boxes):
    l, r = box
    n_pos = r
    while l in l_boxes:
        n_pos = get_next_pos(n_pos, '>')
        if n_pos in walls:
            return False
        if n_pos not in (l_boxes | r_boxes):
            to_move = l
            while to_move != n_pos:
                l_boxes.remove(to_move)
                right = get_next_pos(to_move, '>')
                l_boxes.add(right)
                r_boxes.remove(right)
                r_boxes.add(get_next_pos(right, '>'))
                to_move = get_next_pos(to_move, '>', 2)
    return True

def move_ver(dir, box, walls, l_boxes, r_boxes):
    l, _ = box
    left = {l}
    if try_to_move(dir, left, walls, l_boxes, r_boxes):
        return True
    return False

def try_to_move(dir, left, walls, l_boxes, r_boxes):
    dy = {'^': -1, 'v': +1}.get(dir)
    n_left = set()
    for (lx, ly) in left:
        rx, ry = lx + 1, ly
        if (lx, ly + dy) in walls or (rx, ry + dy) in walls:
            return False
        if (lx, ly + dy) in l_boxes:
            n_left.add((lx, ly + dy))
        elif (lx, ly + dy) in r_boxes:
            n_left.add((lx - 1, ly + dy))
        if (rx, ry + dy) in l_boxes:
            n_left.add((rx , ry + dy))
    if (len(n_left)) == 0:
        for l in left:
            l_boxes.remove(l)
            r_boxes.remove((l[0] + 1, l[1]))
            l_boxes.add((l[0], l[1] + dy))
            r_boxes.add((l[0] + 1, l[1] + dy))
        return True
    else:
        if try_to_move(dir, n_left, walls, l_boxes, r_boxes):
            for l in left:
                r = (l[0] + 1, l[1])
                l_boxes.remove(l)
                r_boxes.remove(r)
                l_boxes.add((l[0], l[1] + dy))
                r_boxes.add((r[0], r[1] + dy))
            return True
        else:
            return False

    

@timed
def main():
    grid, moves = get_input('./input.txt')
    robot = (((len(grid)-1)//2)*2, ((len(grid)-1)//2))
    walls, l_boxes, r_boxes = get_obstacles(grid)
    print_grid(grid, walls, l_boxes, r_boxes, robot)
    for move in moves:
        n_pos = get_next_pos(robot, move)
        if n_pos in walls:
            continue
        if n_pos in (l_boxes | r_boxes):
            # print_grid(grid, walls, l_boxes, r_boxes, robot)
            if move_box(n_pos, move, walls, l_boxes, r_boxes):
                robot = n_pos
            else:
                continue
        robot = n_pos
    print_grid(grid, walls, l_boxes, r_boxes, robot)
    gps_sum = sum(list(map(lambda pos: 100*pos[1] + pos[0], l_boxes)))
    print(gps_sum)

if __name__ == "__main__":
    main()
