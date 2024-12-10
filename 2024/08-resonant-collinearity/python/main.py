from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

antennas = {}

for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char != ".":
            if antennas.get(char) is None:
                antennas[char] = []
            antennas[char].append((x, y))

print("Day 8: Resonant Collinearity (python)")

def findPoints(limit):
    points = []
    for values in antennas.values():
        for i, p in enumerate(values[:-1]):
            for q in values[i+1:]:
                dx, dy = q[0] - p[0], q[1] - p[1]
                if limit:
                    points.append((p[0] - dx, p[1] - dy))
                    points.append((p[0] + 2 * dx, p[1] + 2 * dy))
                    continue
                points.append(p)
                points.append(q)
                multiplier = 2
                while True:
                    x, y = p[0] + multiplier * dx, p[1] + multiplier * dy
                    if x < 0 or y < 0 or x >= len(input[0]) or y >= len(input):
                        break
                    points.append((x, y))
                    multiplier += 1
                multiplier = -1
                while True:
                    x, y = p[0] + multiplier * dx, p[1] + multiplier * dy
                    if x < 0 or y < 0 or x >= len(input[0]) or y >= len(input):
                        break
                    points.append((x, y))
                    multiplier -= 1
    points = set([p for p in points if p[0] >= 0 and p[1] >= 0 and p[0] < len(input[0]) and p[1] < len(input)])
    return points

def printPoints(points):
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if (x, y) in points:
                print("#", end="")
            else:
                print(char, end="")
        print()
    print()

points = findPoints(True)
printPoints(points)
print(f"Part 1: {len(points)}")
points = findPoints(False)
printPoints(points)
print(f"Part 2: {len(points)}")
            