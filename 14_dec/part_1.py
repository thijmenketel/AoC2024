from functools import reduce
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
import re

X = 101
# X = 11
Y = 103
# Y = 7

def get_input(filename):
    with open(filename, 'r') as file:
        robots = []
        for robot in file.read().strip().split('\n'):
            nums = [int(x) for x in re.findall(r'-?\d+', robot)]
            robots.append(([nums[0], nums[1]],(nums[2], nums[3])))
        return robots

def print_grid(robots):
    grid = [['.' for _ in range(X)] for _ in range(Y)]
    for (x, y), _ in robots:
        grid[y][x] = str(int(grid[y][x]) + 1) if grid[y][x] != '.' else '1'
    for row in grid:
        print(''.join(row))
    print('-' * X)


def update_pos(robot):
    (x, y), (dx, dy) = robot
    return (x + dx) % X, (y + dy) % Y

def get_quadrant(robot):
    (x, y), _ = robot
    x_middle = X // 2
    y_middle = Y // 2
    if 0 <= x < x_middle and 0 <= y < y_middle: return 0
    if x_middle < x < X and 0 <= y < y_middle: return 1
    if 0 <= x < x_middle and y_middle < y < Y: return 2
    if x_middle < x < X and y_middle < y < Y: return 3

@timed
def main():
    robots = get_input('./input.txt')
    for _ in range(100):
        for robot in robots:
            robot[0][0], robot[0][1] = update_pos(robot)

    quadrants = {}
    for robot in robots:
        q = get_quadrant(robot)
        if q is not None: quadrants.setdefault(q, []).append(robot[0])

    score = reduce(lambda x, y: x * y, map(lambda n: len(n), quadrants.values()))
    print(score)

if __name__ == "__main__":
    main()
