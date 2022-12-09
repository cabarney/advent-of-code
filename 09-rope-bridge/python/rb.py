from os import path
from collections import namedtuple

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 9: Rope Bridge (python)")

Movement = namedtuple("Movement", ["direction", "distance"])
Position = namedtuple("Position", ["x", "y"])

def parseLine(line):
    parts = line.split(" ")
    return Movement(parts[0], int(parts[1]))

def moveHead(head, direction):
    if direction == "R":
        head = Position(head.x + 1, head.y)
    elif direction == "L":
        head = Position(head.x - 1, head.y)
    elif direction == "U":
        head = Position(head.x, head.y + 1)
    elif direction == "D":
        head = Position(head.x, head.y - 1)
    return head

def moveTail(head, tail):
    distance = ((head.x - tail.x) ** 2 + (head.y - tail.y) ** 2) ** 0.5
    if distance < 2: return tail
    if head.x > tail.x: tail = Position(tail.x + 1, tail.y)
    if head.x < tail.x: tail = Position(tail.x - 1, tail.y)
    if head.y > tail.y: tail = Position(tail.x, tail.y + 1)
    if head.y < tail.y: tail = Position(tail.x, tail.y - 1)
    return tail

def simulateRope(ropeLength):
    positions = [Position(0,0) for _ in range(ropeLength)]
    tailPositions = []
    for line in [parseLine(l) for l in input]:
        for _ in range(line.distance):
            positions[0] = moveHead(positions[0], line.direction)
            for i in range(1,len(positions)):
                positions[i] = moveTail(positions[i-1], positions[i])
            
            tailPositions.append(positions[-1])
    tailPositions = set(tailPositions)
    print(f"The tail of the rope with length {ropeLength} has visited {len(tailPositions)} positions")

simulateRope(2)
simulateRope(10)