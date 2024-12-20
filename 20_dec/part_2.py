import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from part_1 import (
    get_input,
    find_path,
)

def get_ops_for_loc(pos, dist, visited):
    x, y = pos
    for dx in range(x - 20, x + 20 + 1):
        y_range = 20 - abs(dx - x)
        for dy in range(y - y_range, y + y_range + 1):
            if (dx, dy) in dist and (dx, dy) not in visited:
                distance = abs(dx - x) + abs(dy - y)
                yield (dx, dy), distance

@timed
def main():
    _, road, start, end = get_input('./input.txt')
    path, dist = find_path(road, start, end)
    valid_cheats = 0
    e_dist = dist[end]
    visited = set()
    for node in path:
        visited.add(node)
        for opt, steps in get_ops_for_loc(node, dist, visited):
            c_dist = dist[node]
            t_dist = dist[end] - dist[opt]
            if (e_dist - t_dist) - (c_dist + steps) >= 100:
                valid_cheats += 1
    print(valid_cheats)

if __name__ == "__main__":
    main()
