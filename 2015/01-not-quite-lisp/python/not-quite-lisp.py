from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = open(inputPath, 'r').read().strip()

print("Day 1: Not Quite Lisp (python)")

def parseFloorDirection(dir):
    if dir == '(':
        return 1
    elif dir == ')':
        return -1
    else:
        return 0

floor = sum([parseFloorDirection(dir) for dir in input])

print("Part 1:", floor)

floor = 0
position = 0

for dir in input:
    position += 1
    floor += parseFloorDirection(dir)
    if floor == -1:
        break

print("Part 2:", position)
