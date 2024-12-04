from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip().split() for line in open(inputPath, 'r').readlines()]

print("Day 1: Historian Hysteria (python)")

left = []
right = []

for line in input:
    left.append(int(line[0]))
    right.append(int(line[1]))

left.sort()
right.sort()

diff = sum(abs(l - r) for l, r in zip(left, right))
print(f"Difference: {diff}")

print("Part 2")
score = sum(l * right.count(l) for l in left)
print(f"Score: {score}")
