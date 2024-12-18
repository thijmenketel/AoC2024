import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from part_1 import (
    get_input,
    run_dijkstra,
)

@timed
def main():
    corrupted = get_input('./input.txt')
    size, low, high = 71, 1024, len(corrupted)

    while low <= high:
        mid = low + (high - low) // 2
        print(f"{high} {mid} {low}")
        dist = run_dijkstra(corrupted, mid, size)
        if dist == 0: high = mid - 1
        else: low = mid + 1
        if low == mid: print(corrupted[mid-1])

if __name__ == "__main__":
    main()
