from os import path
from functools import cmp_to_key

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

orderings = []
updates = []
idx = input.index("")
orderings = input[:idx]
updates = [update.split(',') for update in input[idx+1:]]

befores = {}
afters = {}
for ordering in orderings:
    before, after = ordering.split("|")
    if before not in befores:
        befores[before] = []
    if after not in afters:
        afters[after] = []
    befores[before].append(after)
    afters[after].append(before)

print("Day 5: Print Queue (python)")

def compare(a, b):
    if a in befores and b in befores[a]:
        return -1
    if a in afters and b in afters[a]:
        return 1
    return 0

correct_order_tot = 0
incorrect_order_tot = 0

for update in updates:
    sorted_update = sorted(update, key=cmp_to_key(compare))
    if all(a == b for a, b in zip(sorted_update, update)):
        correct_order_tot += int(update[int((len(update)-1)/2)])
    else:
        incorrect_order_tot += int(sorted_update[int((len(sorted_update)-1)/2)])


print(correct_order_tot)
print(incorrect_order_tot)
