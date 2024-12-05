import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timer
from part_1 import get_input, get_middle

def get_invalid_pages(pages, rules_dict):
    return filter(lambda page: not is_valid_page(page, rules_dict), pages)

def is_valid_page(page, rules_dict):
    return all(
        is_valid_num(num, rules_dict.get(num, []), page)
        for num in page
        if num in rules_dict
    )

def is_valid_num(num, rules, page):
    return all(
        page.index(num) < page.index(rule)
        for rule in rules
        if rule in page
    )

def sort_pages(pages, rules_dicts):
    left, right = rules_dicts
    sorted = []
    for num in pages:
        if not sorted:
            sorted.append(num)
            continue
        is_before = left.get(num, [])
        is_after = right.get(num, [])
        if not is_before:
            sorted.append(num)
            continue
        curr = 0
        for n in sorted:
            if n in is_after:
                curr += 1
        sorted.insert(curr, num)
    return sorted

def to_dicts(rules):
    rules_dict_left = {}
    rules_dict_right = {}
    for first, second in rules:
        rules_dict_left.setdefault(first, []).append(second)
        rules_dict_right.setdefault(second, []).append(first)
    return rules_dict_left, rules_dict_right

def main():
    rules, pages = get_input('./input.txt')
    rules_dicts = to_dicts(rules)
    sorted_pages = map(
        lambda pages: sort_pages(pages, rules_dicts), 
        get_invalid_pages(pages, rules_dicts[0])
    )
    print(sum(map(get_middle, sorted_pages)))

if __name__ == "__main__":
    with timer():
        main()