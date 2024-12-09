import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timer
from part_1 import get_input

def format_data(data):
    file_id = 0
    new_data, files, free = [], [], []
    for idx, num in enumerate(data):
        if idx % 2 == 0:
            files.append((len(new_data), file_id, num))
            new_data += [file_id for _ in range(num)]
            file_id += 1
        else:
            free.append((len(new_data), num))
            new_data += [-1 for _ in range(num)]
    while files:
        f_loc, id, file_size = files.pop()
        for i, (s_loc, size) in enumerate(free):
            if size >= file_size and s_loc < f_loc:
                for j in range(file_size):
                    new_data[s_loc+j], new_data[f_loc+j] = id, -1
                if size - file_size == 0:
                    free.pop(i)
                else:
                    free[i] = (s_loc+file_size, size - file_size)
                free.pop()
                break
    return new_data

def calc_checksum(data):
    return sum([idx * file_id for idx, file_id in enumerate(data) if file_id != -1])

def main():
    data = get_input('./input.txt')
    new_data = format_data(data)
    print(calc_checksum(new_data))

if __name__ == "__main__":
    with timer():
        main()
