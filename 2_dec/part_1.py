def get_input_as_reports(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.split())) for line in file]

def is_report_safe(report):
    asc = None
    for a,b in list(zip(report[:-1], report[1:])):
        if asc == None: asc = a < b
        if asc and a > b: return False
        if not asc and a < b: return False
        if abs(a-b) > 3 or abs(a-b) < 1: return False
    return True


def main():
    reports = get_input_as_reports('./input.txt')
    print(len(list(filter(is_report_safe, reports))))
    

if __name__ == "__main__":
    main()