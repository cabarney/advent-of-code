from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [[int(x) for x in line.strip().split()] for line in open(inputPath, 'r').readlines()]

print("Day 2: Red-Nosed Reports (python)")

def is_safe(report):
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    if any(d == 0 or abs(d) > 3 for d in diffs):
        return False
    if max(diffs) > 0 and min(diffs) < 0:
        return False
    return True


def is_actually_safe(report):
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True
    return False

print("Part 1")
print(f"Safe Reports: {sum(1 for report in input if is_safe(report))}")

print("Part 2")
print(f"Safe Reports: {sum(1 for report in input if is_actually_safe(report))}")