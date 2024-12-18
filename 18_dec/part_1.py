import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from queue import PriorityQueue

def get_input(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file.read().strip().split('\n')]
        return [tuple(map(int, x.split(','))) for x in lines]

def next(pos, corrupted, size):
    dirs = [(-1, 0),(1, 0), (0, -1),(0, 1)]
    x, y = pos
    return [(x + d[0], y + d[1]) for d in dirs 
            if 0 <= x + d[0] < size and 0 <= y + d[1] < size and (x + d[0], y + d[1]) not in corrupted]

def run_dijkstra(corrupted, max, size):
    q = PriorityQueue()
    q.put((0, (0, 0)))
    visited, distances = set(), {(0, 0): 0}
    while not q.empty():
        curr_dist, curr_node = q.get()
        visited.add(curr_node)
        if curr_node == (size-1, size-1): return curr_dist
        for node in next(curr_node, corrupted[:max], size):
            if node in visited: continue
            if node not in distances or curr_dist + 1 < distances[node]:
                distances[node] = curr_dist + 1
                q.put((curr_dist + 1, node))
    return 0


@timed
def main():
    corrupted = get_input('./input.txt')
    print(run_dijkstra(corrupted, 1024, 71))

if __name__ == "__main__":
    main()
