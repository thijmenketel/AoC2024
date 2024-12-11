import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timer
from math import log10

def get_input(filename):
    with open(filename, 'r') as file:
        return [int(x) for x in file.read().split(' ')]

def get_num_of_digits(num):
    return int(log10(num) + 1) if num != 0 else 1

# super shitty solution, very slow and dumb
def process_numbers(nums):
    idx = 0
    while idx < len(nums):
        num = nums[idx]
        if num == 0:
            nums[idx] = 1
            idx += 1
            continue
        length = get_num_of_digits(num)
        if length % 2 == 0:
            a, b = divmod(num, 10 ** (length // 2))
            nums.pop(idx)
            nums.insert(idx, a)
            nums.insert(idx+1, b)
            idx += 2
            continue
        nums[idx] = num * 2024
        idx +=1
    return nums
            
def main():
    data = get_input('./input.txt')
    for _ in range(25):
        process_numbers(data)
    print(len(data))

if __name__ == "__main__":
    with timer():
        main()
