from itertools import cycle
from os import path
from collections import namedtuple

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 20: Grove Positioning System (python)")

Number = namedtuple("Number", ["orig_idx", "value"])

def parseInput(input, key):
    return [Number(i, int(num) * key) for i, num in enumerate(input)]

def find_curr_idx(numbers, idx):
    return next(i for i, n in enumerate(numbers) if n.orig_idx == idx)

def decrypt(input, key = 1, cnt = 1):
    numbers = parseInput(input, key)
    for mix in range(cnt):
        for i in range(len(numbers)):
            curr_idx = find_curr_idx(numbers, i)
            num = numbers.pop(curr_idx)
            new_idx = (curr_idx + num.value) % len(numbers)
            while new_idx < 0:
                new_idx = len(numbers) + new_idx
            while new_idx >= len(numbers):
                new_idx = new_idx - len(numbers)
            if new_idx == 0 and new_idx < curr_idx:
                numbers.append(num)
            else:
                numbers.insert(new_idx, num)

    idx = next(i for i, n in enumerate(numbers) if n.value == 0)
    # print(idx)
    tot = 0
    for x in [1000, 2000, 3000]:
        i = idx + (x % len(numbers))
        if i >= len(numbers):
            i = i - len(numbers)
        tot += numbers[i].value
        # print(numbers[i].value)
    return tot

print("Part 1:", decrypt(input))
print("Part 2:", decrypt(input, 811589153, 10))
