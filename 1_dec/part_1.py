import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed

def get_input_as_int(filename):
    with open(filename, 'r') as file:
        left, right = zip(*[line.split() for line in file])
    return list(map(int, left)), list(map(int, right))

@timed
def main():
    left, right = get_input_as_int('./input.txt')
    print(sum([abs(l-r) for l,r in list(zip(sorted(left), sorted(right)))]))

if __name__ == "__main__":
    main()