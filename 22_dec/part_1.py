import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from multiprocessing import Pool

def get_input(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def mul_by_64(num): return mix_and_prune(num, num << 6)
def div_by_32(num): return mix_and_prune(num, num >> 5)
def mul_by_2048(num): return mix_and_prune(num, num << 11)
def prune(num): return num % 16777216
def mix(num, mixer): return num ^ mixer
def mix_and_prune(num, mixer): return prune(mix(num, mixer))

def iterate(num): return mul_by_2048(div_by_32(mul_by_64(num)))

def permutatate_by(iterations, num):
    for _ in range(iterations):
        num = iterate(num)
    return num

@timed
def main():
    data = get_input('./input.txt')
    with Pool(10) as pool:
        print(sum(pool.starmap(permutatate_by, [(2000, num) for num in data])))

if __name__ == "__main__":
    main()
