import re

def get_input_as_string(filename):
    with open(filename, 'r') as file:
        return file.read()

def get_all_matching_substrings(string):
    pattern = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
    return pattern.findall(string)

def main():
    reports = get_input_as_string('./input.txt')
    print(sum(map(mul.multiply, map(eval, get_all_matching_substrings(reports)))))

class mul(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def multiply(self):
        return self.first * self.second

if __name__ == "__main__":
    main()