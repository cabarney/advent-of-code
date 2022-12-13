from collections import namedtuple
import functools
import itertools
from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = open(inputPath, 'r').read().split("\n\n")
pairs = [[l.strip() for l in line.splitlines()] for line in input]

print("Day 13: Distress Signal (python)")

def compare(left, right):
    if left == None or right == None:
        if left == None:
            if right == None: return 0
            return -1
        else: return 1

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    result = 0
    for l,r in itertools.zip_longest(left, right, fillvalue=None):
        if isinstance(l, int) and isinstance(r, int):
            if l == r: continue
            result = l - r
            break
        elif type(l) != type(r):
            c = compare(l, r)
            if c == 0: continue
            result = c
            break
        else: 
            c = compare(l, r)
            if c == 0: continue
            result = c
            break
    return result

def compareStr(left, right): return compare(eval(left), eval(right))

print("Part 1:", sum(i+1 for i, pair in enumerate(pairs) if compareStr(pair[0], pair[1]) < 0))

dividers = ["[[2]]", "[[6]]"]
all = list(itertools.chain(*pairs, dividers))
allSorted = sorted(all, key=functools.cmp_to_key(compareStr))
dividerIndices = [i + 1 for i, x in enumerate(allSorted) if x in dividers]

print("Part 2:", dividerIndices[0] * dividerIndices[1])
