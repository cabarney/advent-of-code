from os import path
from collections import namedtuple

Location = namedtuple("Location", ["x", "y", "z"])

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
# inputPath = path.abspath(path.join(basepath, "..", "ex.txt"))
input = {Location(*[int(x) for x in line.strip().split(",")]) for line in open(inputPath, 'r').readlines()}

print("Day 18: Boiling Boulders (python)")
borders = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]

exposedSides = 0

for cube in input:
    borderingLocations = {Location(cube.x + border[0], cube.y + border[1], cube.z + border[2]) for border in borders}
    borderingCubes = input.intersection(borderingLocations)
    exposedSides += 6 - len(borderingCubes)

print("Part 1:", exposedSides)
