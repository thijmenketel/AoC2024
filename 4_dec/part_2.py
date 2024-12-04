from part_1 import get_input_as_string

def is_MAS(string):
    return string in ['SAM', 'MAS']

def has_XMAS(i, j, text):
    if text[i][j] != 'A': return False
    diag_lr = f"{text[i-1][j-1]}A{text[i+1][j+1]}"
    diag_rl = f"{text[i+1][j-1]}A{text[i-1][j+1]}"
    return is_MAS(diag_lr) and is_MAS(diag_rl)

def count_text(text):
    size = len(text)
    total = 0
    for i in range(1, size-1):
        for j in range(1, size-1):
            if has_XMAS(i, j, text):
                total += 1
    return total

def main():
    text = get_input_as_string('./input.txt')
    print(count_text(text))

if __name__ == "__main__":
    main()