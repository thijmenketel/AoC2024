
def get_input_as_int(filename):
    with open(filename, 'r') as file:
        left, right = zip(*[line.split() for line in file])
    return list(map(int, left)), list(map(int, right))

def main():
    left, right = get_input_as_int('./input.txt')
    total_score = sum([l * right.count(l) for l in left])

    print(total_score)

if __name__ == "__main__":
    main()