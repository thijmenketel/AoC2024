import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timer

def get_input(filename):
    with open(filename, 'r') as file:
        rules, pages = file.read().split('\n\n')
        rules = [tuple(map(int, rule.split('|'))) for rule in rules.split('\n')]
        pages = [list(map(int, page.split(','))) for page in pages.split('\n')]
    return rules, pages

def is_valid_num(num, rules, page):
    return all(
        page.index(num) < page.index(rule[1])
        for rule in rules
        if rule[1] in page
    )
    
def is_valid_page(page, rules_dict):
    return all(
        is_valid_num(num, rules_dict.get(num, []), page)
        for num in page
        if num in rules_dict
    )

def get_middle(page):
    return page[(len(page) - 1) // 2]

def to_dict(rules):
    rules_dict = {}
    for first, second in rules:
        rules_dict.setdefault(first, []).append((first, second))
    return rules_dict
            
def main():
    rules, pages = get_input('./input.txt')
    rules_dict = to_dict(rules)
    correct_pages = list(filter(lambda page: is_valid_page(page, rules_dict), pages))
    print(sum(map(get_middle, correct_pages)))

if __name__ == "__main__":
    with timer():
        main()