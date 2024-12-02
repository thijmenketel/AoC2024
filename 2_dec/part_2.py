from part_1 import get_input_as_reports, is_report_safe

def is_mutated_report_safe(report):
    if is_report_safe(report): return True
    for idx in range(0, len(report)):
        subreport = [num for sub_idx, num in enumerate(report) if idx != sub_idx]
        if is_report_safe(subreport): return True
    return False

def main():
    reports = get_input_as_reports('./input.txt')
    print(len(list(filter(is_mutated_report_safe, reports))))

if __name__ == "__main__":
    main()