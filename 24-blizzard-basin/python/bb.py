import math
from os import path
from collections import deque

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 24: Blizzard Basin (python)")

def mapDirection(dir):
    if dir == "^":
        return (0, -1)
    elif dir == "v":
        return (0, 1) 
    elif dir == ">":
        return (1, 0)
    elif dir == "<":
        return (-1, 0)
    else:
        raise Exception("Unknown direction: " + dir)

def print_grid(width, height, blizzards, time, cx, cy):
    # print(blizzards)
    def map_reverse(dir):
        if dir == (0, -1):
            return "^"
        elif dir == (0, 1):
            return "v"
        elif dir == (1, 0):
            return ">"
        elif dir == (-1, 0):
            return "<"
        else:
            raise Exception("Unknown direction: " + dir)

    print("#" + ("E" if (cx, cy) == (0, -1) else ".") + "#" * width)
    # blizzard_locations = {((b[0] + b[2][0] * time) % (width), (b[1] + b[2][1] * time) % height): map_reverse(b[2]) for b in blizzards}
    for y in range(height):
        print("#", end="") 
        for x in range(width):
            if x == cx and cy == y:
                print("E", end="")
            # elif (x, y) in blizzard_locations:
            #     print(blizzard_locations[(x, y)], end="")
            else:
                b_loc = []
                for bx, by in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    if ((x - bx * time) % width, (y - by * time) % height) in blizzards[(bx, by)]:
                        b_loc.append(map_reverse((bx, by)))
                if len(b_loc) == 0:
                    print(".", end="")
                else:
                    print(b_loc[0] if len(b_loc) == 1 else len(b_loc), end="")
        print("#")
    print(("#" * width) + ("E" if (cx, cy) == (width - 1, height) else ".") + "#")
    print()
    print()

def parseInput(input):
    height = len(input) - 2
    width = len(input[1]) - 2

    blizards = dict({(0, -1): set(), (0, 1): set(), (-1, 0): set(), (1, 0): set()})
    for iline, line in enumerate(input[1:]):
        for icol, col in enumerate(line[1:]):
            if col in "<>^v":
                blizards[mapDirection(col)].add((icol, iline))

    return (width, height, blizards)

def bfs(blizzards, target, width, height, startx, starty, time):
    seen = set()
    queue = deque([(time,startx,starty)])
    lcm = width * height // math.gcd(width, height)

    # print_grid(width, height, blizzards, 0, 0, -1)
    while queue:
        t, x, y = queue.popleft()
        t += 1

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1), (0,0)]:
            nx = x + dx
            ny = y + dy
            if (nx, ny) == target:
                return t
            if (nx < 0 or nx >= width or ny < 0 or ny >= height) and not (nx, ny) == (0,-1):
                continue
            isBlizzard = False
            if (nx, ny) != (0,-1):
                for bx, by in [(0,-1),(0,1),(-1,0),(1,0)]: 
                    if ((nx - bx * t) % width, (ny - by * t) % height) in blizzards[(bx,by)]:
                        isBlizzard = True
                        break
                # for b in blizzards:
                #     if (nx, ny) == ((b[0] + (b[2][0] * t) % width), (b[1] + (b[2][1] * t) % height)):
                #         isBlizzard = True
                #         break
            if isBlizzard:
                continue
            if (t % lcm, nx, ny) in seen:
                continue
            # print_grid(width, height, blizzards, t, nx, ny)
            seen.add((t % lcm, nx, ny))
            queue.append((t, nx, ny))


# width, height, target, blizzards = parseInput(input)
# for t in range(10):
#     print_grid(width, height, blizzards, t, 0, -1)

width, height, blizzards = parseInput(input)
p1_time = bfs(blizzards, (width - 1, height), width, height, 0, -1, 0)
print("Part 1: " + str(p1_time))

p2_time = bfs(blizzards, (0, -1), width, height, width - 1, height, p1_time)
p2_time = bfs(blizzards, (width - 1, height), width, height, 0, -1, p2_time)
print("Part 2: " + str(p2_time))
