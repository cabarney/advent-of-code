from collections import deque, namedtuple
from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 12: Hill Climbing Algorithm (python)")

Point = namedtuple('Point', ['x', 'y'])

grid = [list([ord(cell) for cell in line]) for line in input]

def findValue(value):
    return [Point(row.index(value), y) for y, row in enumerate(grid) if value in row][0]

def findAllValues(value):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in value:
                yield Point(x, y)

def height(x, y): 
    if grid[y][x] == ord("S"): return ord("a")
    if grid[y][x] == ord("E"): return ord("z")
    return grid[y][x]

def enumerateDirections(x, y):
    if x > 0: yield Point(x-1, y)
    if x < len(grid[0]) - 1: yield Point(x+1, y)
    if y > 0: yield Point(x, y-1)
    if y < len(grid) - 1: yield Point(x, y+1)

def findPossibleMoves(point):
    h = height(point.x, point.y)
    return [move for move in enumerateDirections(point.x, point.y) if height(*move) <= h+1]

end = findValue(ord("E"))

def initDistances(start):
    distances = {}
    for y, r in enumerate(grid):
        for x, c in enumerate(r):
            distances[Point(x, y)] = 2 ** 32
    distances[start] = 0
    return distances


def findPathLength(start):    
    distances = initDistances(start)    
    visited = set()
    queue = deque()
    queue.append(start)
    while len(queue) > 0:
        point = queue.popleft()
        visited.add(point)
        moves = findPossibleMoves(point)
        if end in moves:
            return distances[point] + 1
        for move in moves:
            # print(point, distances[point], move, distances[move])
            distances[move] = min(distances[move], distances[point] + 1)
            if move not in visited and move not in queue:
                queue.append(move)
    
    return 2 ** 32


print(findPathLength(findValue(ord("S"))))

print(min(findPathLength(p) for p in [p for p in findAllValues([ord("a")])]))
