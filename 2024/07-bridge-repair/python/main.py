from os import path
from itertools import product

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

eqs = []

for line in input:
    parts = line.split(":")
    tot = int(parts[0])
    vals = [int(x) for x in parts[1].split()]
    eqs.append((tot, vals))


print("Day 7: Bridge Repair (python)")


def eval_eq(eq, opers) -> int:
    ops_possibilities = list(product(opers, repeat=len(eq[1])-1))
    for poss in ops_possibilities:
        tot = eq[1][0]
        for i, op in enumerate(poss):
            if op == "+":
                tot += eq[1][i+1]
            elif op == "*":
                tot *= eq[1][i+1]
            elif op == "|":
                tot = int(str(tot) + str(eq[1][i+1]))
        if tot == eq[0]:
            return tot
    return 0

p1 = sum(eval_eq(eq, ["+", "*"]) for eq in eqs)
print("Part 1:", p1)
p2 = sum(eval_eq(eq, ["+", "|", "*"]) for eq in eqs)
print("Part 2:", p2)