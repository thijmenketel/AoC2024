import sys
import os
from tokenize import group

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from queue import PriorityQueue
from part_1 import (
    get_input,
    print_grid,
    find_neighbours
)

def run_dijkstra(grid, start, end, shortest = sys.maxsize, start_score = 0, dir = '>'):
    visited, distances = set(), {start: 0}
    priority_queue = PriorityQueue()
    priority_queue.put((start_score, (start, dir)))
    pred = {start: (None, None, None)}
    while not priority_queue.empty():
        curr_dist, (curr_node, curr_dir) = priority_queue.get()
        visited.add(curr_node)
        if curr_dist > shortest:
            return curr_dist, []
        if curr_node == end:
            path = []
            current = end, curr_dir, curr_dist
            while current != (None, None, None):
                path.append(current)
                current = pred.get(current[0])
            return curr_dist, list(reversed(path))
        for dist, (next_node, ndir) in find_neighbours(grid, curr_node, curr_dir):
            if next_node in visited:
                continue
            new_dist = curr_dist + dist
            if next_node not in distances or new_dist < distances[next_node]:
                distances[next_node] = new_dist
                pred[next_node] = (curr_node, curr_dir, curr_dist)
                priority_queue.put((new_dist, (next_node, ndir)))
    return 0, []

@timed
def main():
    grid = get_input('./input.txt')
    size = len(grid)
    start, end = (1, size-2), (size-2, 1)
    shortest_path, path = run_dijkstra(grid, start, end)
    seats = set([x[0] for x in path])
    for node, dir, score in path:
        opts = find_neighbours(grid, node, dir)
        for dist, (pos, ndir) in opts:
            if pos in seats:
                continue
            new_score, new_path = run_dijkstra(grid, pos, end, shortest_path, score + dist, ndir)
            if new_score != shortest_path:
                continue
            seats.update([x[0] for x in new_path])
    # print_grid(grid, seats)
    print(shortest_path)
    print(len(seats))

if __name__ == "__main__":
    main()
