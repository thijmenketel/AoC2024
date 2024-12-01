

def get_input_as_int(filename):
    with open(filename, 'r') as file:
        left, right = zip(*[line.split() for line in file])
    return list(map(int, left)), list(map(int, right))

def get_distance(a, b):
    return abs(a-b)

left, right = get_input_as_int('./input.txt')
print(sum([get_distance(l, r) for l,r in list(zip(sorted(left), sorted(right)))]))