from part_1 import (
    get_input, 
    get_middle, 
    is_valid_page, 
    is_valid_num, 
    to_dict
)

def get_invalid_pages(pages, rules_dict):
    return filter(lambda page: not is_valid_page(page, rules_dict), pages)

def sort_page(page, rules_dict):
    copy = page[:]
    while not is_valid_page(copy, rules_dict):
        for num in page:
            if num not in rules_dict: continue
            for idx in range(len(page)):
                if not is_valid_num(num, rules_dict[num], copy):
                    copy.insert(idx, copy.pop(copy.index(num)))
    return copy
            
def main():
    rules, pages = get_input('./input.txt')
    rules_dict = to_dict(rules)
    sorted_pages = map(
        lambda page: sort_page(page, rules_dict), 
        get_invalid_pages(pages, rules_dict)
    )
    print(sum(map(get_middle, sorted_pages)))

if __name__ == "__main__":
    main()