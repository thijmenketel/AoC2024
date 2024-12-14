import sys
import os
from time import sleep

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from part_1 import (
    get_input,
    print_grid,
    update_pos,
)

@timed
def main():
    robots = get_input('./input.txt')
    for i in range(10000):
        print_grid(robots)
        for robot in robots:
            robot[0][0], robot[0][1] = update_pos(robot)
        print(f"----------------- {i} ------------------")
        sleep(0.1)

if __name__ == "__main__":
    main()
