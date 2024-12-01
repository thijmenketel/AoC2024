

def get_input_as_int(filename):
    with open(filename, 'r') as file:
        left, right = zip(*[line.split() for line in file])
    return list(map(int, left)), list(map(int, right))


left, right = get_input_as_int('./input.txt')

score_map = {}
total_score = 0

for l in left:
    if (l in score_map):
        total_score += score_map[l]
    else:
        score = l * right.count(l)
        score_map[l] = score
        total_score += score

print(total_score)