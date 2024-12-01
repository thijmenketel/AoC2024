

def get_input_as_int(filename):
    with open(filename, 'r') as file:
        left, right = zip(*[line.split() for line in file])
    return list(map(int, left)), list(map(int, right))

def main():
    left, right = get_input_as_int('./input.txt')
    print(sum([abs(l-r) for l,r in list(zip(sorted(left), sorted(right)))]))

if __name__ == "__main__":
    main()