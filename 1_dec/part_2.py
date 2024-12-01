from part_1 import get_input_as_int

def main():
    left, right = get_input_as_int('./input.txt')
    total_score = sum([l * right.count(l) for l in left])

    print(total_score)

if __name__ == "__main__":
    main()