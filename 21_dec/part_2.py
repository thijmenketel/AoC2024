import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from functools import cache
from part_1 import (
    get_input,
    get_dirs_for_code,
)

def get_moves(start, end):
    if start == end: return 'A'
    return {
        ('A', '<'): 'v<<A',
        ('A', '^'): '<A',
        ('A', '>'): 'vA',
        ('A', 'v'): '<vA',
        ('<', 'A'): '>>^A',
        ('<', 'v'): '>A',
        ('<', '^'): '>^A',
        ('<', '>'): '>>A',
        ('v', 'A'): '^>A',
        ('v', '<'): '<A',
        ('v', '^'): '^A',
        ('v', '>'): '>A',
        ('>', 'A'): '^A',
        ('>', 'v'): '<A',
        ('>', '<'): '<<A',
        ('>', '^'): '<^A',
        ('^', 'A'): '>A',
        ('^', 'v'): 'vA',
        ('^', '<'): 'v<A',
        ('^', '>'): 'v>A',
    }[(start, end)]

@cache
def get_next_seq(seq):
    new, curr = [], 'A'
    for d in seq:
        new.append(get_moves(curr, d))
        curr = d
    return new

@cache
def DFS(seq, depth):
    if depth == 0: return len(seq)
    return sum([DFS(s, depth - 1) for s in get_next_seq(seq)])

@timed
def main():
    codes = get_input('./input.txt')
    complexity = 0
    for code in codes:
        dirs = get_dirs_for_code(code)
        size = sum([DFS(moves, 25) for moves in dirs.split()])
        complexity += size * int(code.strip('A'))
    print(complexity)

if __name__ == "__main__":
    main()
