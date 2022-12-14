from collections import namedtuple
from os import path
import functools

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 14: Regolith Reservoir (python)")

Point = namedtuple("Point", ["x", "y"])

class Grid:
    _grid: list[list[str]] = [[]]

    def __init__(self, input, hasFloor):        
        lines: list[list[Point]] = []

        maxY = 0
        for line in input:
            lineCoords = [(Point(int(pair[0]), int(pair[1]))) for pair in [c.split(",") for c in line.split(" -> ")]]
            lines.append(lineCoords)

        maxY = max([point.y for line in lines for point in line])

        self._grid = [["." for _ in range(1000)] for _ in range(maxY + 2)]
        self._grid[0][500] = "+"
        
        for line in lines:
            functools.reduce(lambda p1, p2: self.drawLine(p1, p2), line[1:], line[0])

        self._grid.append(["#" if hasFloor else "." for _ in range(1000)])
    
    def drawLine(self, point1, point2):
        if point1.x == point2.x:
            for y in range(min(point1.y, point2.y), max(point1.y, point2.y)+1):
                self._grid[y][point1.x] = "#"
        else:
            for x in range(min(point1.x, point2.x), max(point1.x, point2.x)+1):
                self._grid[point1.y][x] = "#"
        return point2

    def get(self, point):
        return self._grid[point.y][point.x]

    def set(self, point, value):
        self._grid[point.y][point.x] = value

    def get_rowCount(self):
        return len(self._grid)

    def get_columnCount(self):
        return len(self._grid[0])

    def get_sand(self):
        return "".join([x for row in self._grid for x in row]).count("o")

    def print(self):
        relevantRows = ["".join(row).replace("#", "x").replace("o", "x").replace("+", "x") for row in self._grid if any([x in row for x in ["#", "o", "+"]])][:-1]
        minX = min(row.index("x") for row in relevantRows)
        maxX = len(self._grid[0]) - min(row[::-1].index("x") for row in relevantRows)
        for row in self._grid:
            print("".join(row[minX-1:maxX+2]))

    totalSand = property(get_sand)
    rowCount = property(get_rowCount)
    columnCount = property(get_columnCount)

class Sand:
    def __init__(self, grid: Grid, point):
        self.position = point
        self._grid = grid

    def __atBottom(self):
        return self.position.y == self._grid.rowCount - 1

    def __findMove(self):
        if self.__atBottom(): return None
        if self._grid.get(self.position) == "o": return None

        moves = []
        for move in [Point(*map(sum, zip(self.position, m))) for m in [Point(0, 1), Point(-1, 1), Point(1, 1)]]:
            moves.append((Point(*move), self._grid.get(Point(*move))))

        if all(map(lambda x: x[1] == "#" or x[1] == "o", moves)):
            return "o"

        move = next(filter(lambda x: x[1] == ".", moves))

        return move[0]

    def reset(self, point):
        self.position = point

    def move(self):
        move = self.__findMove()
        while move:
            if move == "o":
                self._grid.set(self.position, "o")
                return True
            self.position = move
            move = self.__findMove()
        return False

source = Point(500, 0)

def separator(): print("=====================================")

def simulate(grid: Grid):
    sand = Sand(grid, source)
    while sand.move(): sand.reset(source)
    grid.print()
    print("TOTAL SAND:", grid.totalSand)    
    separator()


grid = Grid(input, False)
simulate(grid)
grid = Grid(input, True)
simulate(grid)
