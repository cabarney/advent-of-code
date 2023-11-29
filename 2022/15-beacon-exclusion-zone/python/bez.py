from collections import namedtuple
from os import path
import time
import multiprocessing as mp

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 15: Beacon Exclusion Zone (python)")

Point = namedtuple("Point", ["x", "y"])

def getDistance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def parseLine(line):
    pairs = line[12:].replace("closest beacon is at", "").replace(" ", "").replace("x=", "").replace("y=", "").split(":")
    p1, p2 = pairs[0].split(","), pairs[1].split(",")
    return Point(int(p1[0]), int(p1[1])), Point(int(p2[0]), int(p2[1]))

def parseInput(input):
    return [(coords[0], coords[1], getDistance(*coords)) for coords in [parseLine(line) for line in input]]

def coveredBySensorOnLine(sensors, y):
    covered = set()
    for sensor in [s for s in sensors if abs(y - s[0].y) <= s[2]]:
        dy = abs(sensor[0].y - y)
        dx = sensor[2] - dy
        covered.update(range(sensor[0].x - dx, sensor[0].x + dx + 1))
    covered.difference_update([sensor[1].x for sensor in sensors if sensor[1].y == y])
    return covered

def coveredRanges(sensors, y, maxRange):
    for sensor in [s for s in sensors]:
        dy = abs(sensor[0].y - y)
        if dy > sensor[2]:
            continue
        dx = sensor[2] - dy
        yield [max(0, sensor[0].x - dx), min(maxRange, sensor[0].x + dx)]

def findBeaconTuningFrequency(sensors, maxRange):
    for y in range(0, maxRange + 1):
        ranges = sorted(coveredRanges(sensors, y, maxRange))
        maxX = 0
        for i in range(0, len(ranges) - 1):
            maxX = max(maxX, ranges[i][1])
            if maxX+1 < ranges[i+1][0]:
                return (ranges[i][1]+1) * maxRange + y

sensors = parseInput(input)

start = time.time()
print("Part 1:", len(coveredBySensorOnLine(sensors, 2_000_000)), end=" -> ")
stop = time.time()
print("Time:", stop - start)

start = time.time()
print("Part 2:", findBeaconTuningFrequency(sensors, 400_000_000), end=" -> ")
stop = time.time()
print("Time:", stop - start)
