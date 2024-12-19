import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed

def get_input(filename):
    with open(filename, 'r') as file:
        data = file.read().strip().split('\n\n')
        return tuple(data[0].split(', ')), data[1].split('\n')

def can_make_towel(towel, stripes):
    for stripe in stripes:
        if not towel.startswith(stripe): continue
        next = towel[len(stripe):]
        if not next: return True
        if can_make_towel(next, stripes):
            return True
    return False

@timed
def main():
    stripes, towels = get_input('./input.txt')
    num = filter(lambda x:x, map(lambda towel: can_make_towel(towel, stripes), towels))
    print(len(list(num)))

if __name__ == "__main__":
    main()
