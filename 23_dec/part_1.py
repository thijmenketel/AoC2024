import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from collections import defaultdict

def get_input(filename):
    with open(filename, 'r') as file:
        conns = [line.split('-') for line in file.read().strip().split('\n')]
        conn_map = defaultdict(set)
        for start, end in conns:
            conn_map[start].add(end)
            conn_map[end].add(start)
        return conn_map

@timed
def main():
    conn_map = get_input('./input.txt')
    cycles = set()
    for start, cons1 in conn_map.items():
        for hop1 in cons1:
            for hop2 in conn_map[hop1]:
                if start in conn_map[hop2]:
                    cycles.add(tuple(sorted([start, hop1, hop2])))
    cycles = set(filter(lambda cycle: any(c.startswith('t') for c in cycle), cycles))
    print(len(cycles))

if __name__ == "__main__":
    main()
