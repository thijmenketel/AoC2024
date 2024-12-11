import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed

def get_input(filename):
    with open(filename, 'r') as file:
        return [int(x) for x in file.read()]

def format_data(data):
    files, free = data[::2], data[1::2]
    r_id, f_id = len(files) - 1, 1
    new_data = [0 for _ in range(files.pop(0))]
    filler = []
    while files:
        space = free.pop(0)
        for _ in range(space):
            if not filler:
                filler = [r_id for _ in range(files.pop())]
                r_id -= 1
            new_data.append(filler.pop(0))
        if files:
            new_data += [f_id for _ in range(files.pop(0))]
            f_id += 1
    new_data += filler
    return new_data

def calc_checksum(data):
    return sum([id * num for id, num in enumerate(data)])

@timed
def main():
    data = get_input('./input.txt')
    new_data = format_data(data)
    print(calc_checksum(new_data))

if __name__ == "__main__":
    main()
