
def get_input_as_string(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
    
def count_xmas(string):
    return string.count("XMAS")

def get_diagonal(text):
    diags = []
    size = len(text)
    limit = size * 2 - 1
    for round in range(limit):
        ver = round if round < size else size - 1
        hor = 0 if round < size else round - size + 1
        diag = ""
        while hor <= round and hor < size:
            diag += text[ver][hor]
            ver -= 1
            hor += 1
        if len(diag) > 3: diags.append(diag)
    return diags

def reverse_text(text):
    return [x[::-1] for x in text]

def count_text(text):
    transposed = [''.join(list(x)) for x in zip(*text)]
    diagonal_lr = get_diagonal(text)
    diagonal_rl = get_diagonal([x[::-1] for x in text])
    options = [
        *text,
        *reverse_text(text),
        *transposed,
        *reverse_text(transposed),
        *diagonal_lr,
        *reverse_text(diagonal_lr),
        *diagonal_rl,
        *reverse_text(diagonal_rl)
    ]
    return sum(map(count_xmas, options))

def main():
    text = get_input_as_string('./input.txt')
    print(count_text(text))

if __name__ == "__main__":
    main()