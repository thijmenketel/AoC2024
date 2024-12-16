import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from itertools import product
from queue import PriorityQueue

def get_input(filename):
    with open(filename, 'r') as file:
        return [[x for x in line] for line in file.read().strip().split('\n')]

def print_grid(grid, path):
    size = len(grid)
    for y, x in product(range(size), range(size)):
        if (x, y) in path:
            grid[y][x] = 'O'
    for row in grid:
        print(''.join(row))
    print('-' * size)

def run_dijkstra(grid, start, end):
    visited, distances = set(), {start: 0}
    priority_queue = PriorityQueue()
    priority_queue.put((0, (start, '>')))
    pred = {start: None}
    while not priority_queue.empty():
        curr_dist, (curr_node, curr_dir) = priority_queue.get()
        visited.add(curr_node)
        if curr_node == end:
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = pred.get(current)
            return curr_dist, list(reversed(path))
        for dist, (next_node, ndir) in find_neighbours(grid, curr_node, curr_dir):
            if next_node in visited:
                continue
            new_dist = curr_dist + dist
            if next_node not in distances or new_dist < distances[next_node]:
                distances[next_node] = new_dist
                pred[next_node] = curr_node
                priority_queue.put((new_dist, (next_node, ndir)))
    return distances

def find_neighbours(grid, pos, curr_dir):
    dirs = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
    x, y = pos
    neighbors = []
    for key, dir in dirs.items():
        node = grid[y+dir[1]][x+dir[0]]
        match node:
            case '#': continue
            case '.'|'E'|'S':
                neighbors.append((1 if key == curr_dir else 1001, ((x+dir[0], y+dir[1]), key)))
    return neighbors


@timed
def main():
    grid = get_input('./input.txt')
    size = len(grid)
    start, end = (1, size-2), (size-2, 1)
    shortest_path, path = run_dijkstra(grid, start, end)
    # print_grid(grid, path)
    print(shortest_path)

if __name__ == "__main__":
    main()
