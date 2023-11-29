from os import path
import itertools
import re

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
# inputPath = path.abspath(path.join(basepath, "..", "ex.txt"))
input = [line.replace("\n", "") for line in open(inputPath, 'r').readlines()]
directions = [(1, 0, ">"), (0, 1, "v"), (-1, 0, "<"), (0, -1, "^")]

print("Day 22: Monkey Map (python)")

def print_map(map, x = None, y = None):
    print()
    for i, line in enumerate(map):
        for j, c in enumerate(line):
            if x == j and y == i:
                print("@", end="")
            else:
                print(c, end="")
        print()
    print()


def parseInput(input):
    map = input[:-2]
    w = max([len(line) for line in map])
    map = [list(line.ljust(w)) for line in map]

    path = input[-1]
    nums = re.findall(r"(\d+)", path)
    dirs = re.findall(r"([LR])", path)
    
    path = list(itertools.chain(*zip(nums, dirs))) + [nums[-1]]
    return map, path


def get_map_info(map):
    h = len(map)
    w = len(map[0])
    return w, h, h > w


def get_face(map, x, y):
    w, h, port = get_map_info(map)
    face_mapping = [[0, 1, 2], 
                    [0, 3, 0], 
                    [4, 5, 0], 
                    [6, 0, 0]
                    ] if port else [
                    [0, 0, 1, 0], 
                    [2, 3, 4, 0], 
                    [0, 0, 5, 6]]
    return face_mapping[y//(h//4)][x//(w//3)] if port else face_mapping[y//(h//3)][x//(w//4)]


def get_face_bounds(map):
    w, h, port = get_map_info(map)
    face_w = w//3 if port else w//4
    face_h = h//4 if port else h//3
    face_locations = [(), (1,0), (2,0), (1,1), (0,2), (1,2), (0,3)] if port else [(), (2,0), (0,1), (1,1), (2,1), (2,2), (3,2)]
    for face in range(1, 7):
        x1, y1 = face_locations[face]
        x1 *= face_w
        y1 *= face_h
        x2 = x1 + face_w
        y2 = y1 + face_h
        yield face, (x1, y1), (x2 - 1, y2 - 1)


def get_face_by_id(map, id):
    return next(info for info in get_face_bounds(map) if info[0] == id)


def get_face_info(map, x, y):
    face_id = get_face(map, x, y)
    return get_face_by_id(map, face_id)


def find_next_location_3d(map, x, y, dir):
    _, _, port = get_map_info(map)
    face, p1, p2 = get_face_info(map, x, y)
    nextx, nexty = x, y

    if (x == p1[0] and dir == 2) or (x == p2[0] and dir == 0) or (y == p1[1] and dir == 3) or (y == p2[1] and dir == 1):
        # On the edge of the face
        face_wrapping = [[],[(2, 0), (3, 1), (4, 0), (6, 0)],
                            [(5, 2), (3, 2), (1, 2), (6, 3)],
                            [(2, 3), (5, 1), (4, 1), (1, 3)],
                            [(5, 0), (6, 1), (1, 0), (3, 0)],
                            [(2, 2), (6, 2), (4, 2), (3, 3)],
                            [(5, 3), (2, 1), (1, 1), (4, 3)] 
                            ] if port else [[],
                            [(6, 2), (4, 1), (3, 1), (2, 1)],
                            [(3, 0), (5, 3), (6, 3), (1, 1)],
                            [(4, 0), (5, 0), (2, 2), (1, 0)],
                            [(6, 1), (5, 1), (3, 2), (1, 3)],
                            [(6, 0), (2, 3), (3, 3), (4, 3)],
                            [(1, 2), (2, 0), (5, 2), (4, 2)]]
        newFace, dir_next = face_wrapping[face][dir]
        _, p1_next, p2_next = get_face_by_id(map, newFace)

        if dir == dir_next:
            if dir == 0: 
                nextx, nexty = p1_next[0], p1_next[1] + y - p1[1]
            elif dir == 1: 
                nextx, nexty = p1_next[0] + x - p1[0], p1_next[1]
            elif dir == 2:
                nextx, nexty = p2_next[0], p1_next[1] + y - p1[1]
            elif dir == 3: 
                nextx, nexty = p1_next[0] + x - p1[0], p2_next[1]
        elif abs(dir - dir_next) == 2:
            if dir % 2 == 0:
                nextx = p1_next[0] if dir_next == 0 else p2_next[0]
                nexty = p2[1] - y + p1_next[1]
            else:
                nextx = p2[0] + x - p1[0]
                nexty = p1_next[1] if dir_next == 1 else p2_next[1]
        else:
            if dir == 0 and dir_next == 1:
                nextx = p1_next[0] + p2[1] - y
                nexty = p1_next[1]
            elif dir == 0 and dir_next == 3:
                nextx = p1_next[0] + y - p1[1]
                nexty = p2_next[1]
            elif dir == 1 and dir_next == 0:
                nextx = p1_next[0]
                nexty = p1_next[1] + p2[0] - x
            elif dir == 1 and dir_next == 2:
                nextx = p2_next[0]
                nexty = p1_next[1] + x - p1[0]
            elif dir == 2 and dir_next == 1:
                nextx = p2_next[0] + y - p2[1]
                nexty = p1_next[1]
            elif dir == 2 and dir_next == 3:
                nextx = p1_next[0] + p1[1] - y
                nexty = p2_next[1]
            elif dir == 3 and dir_next == 0:
                nextx = p1_next[0]
                nexty = p1_next[1] + x - p1[0]
            elif dir == 3 and dir_next == 2:
                nextx = p2_next[0]
                nexty = p1_next[1] + p2[0] - x
        return nextx, nexty, dir_next
    else:
        return x + directions[dir][0], y + directions[dir][1], dir
        

def find_next_location_2d(map, x, y, dir):
    nextx, nexty = x + directions[dir][0], y + directions[dir][1]
    if nextx < 0 or nextx >= len(map[0]) or nexty < 0 or nexty >= len(map) or map[nexty][nextx] == " ":            
        if dir == 0:
            nextx = next(i for i, c in enumerate(map[y]) if c != " ")
        elif dir == 2:
            nextx = len(map[y]) - next(i for i, c in enumerate(map[y][::-1]) if c != " ") - 1
        elif dir == 1:
            nexty = next(i for i, c in enumerate(row[x] for row in map) if c != " ")
        else:
            nexty = len(map) - next(i for i, c in enumerate([row[x] for row in map][::-1]) if c != " ") - 1
    return nextx, nexty, dir


def move(map, x, y, dir, distance, use3d = False):
    for _ in range(distance):       
        nextx, nexty, nextdir = find_next_location_3d (map, x, y, dir) if use3d else find_next_location_2d(map, x, y, dir)
        if map[nexty][nextx] == "#":
            return x, y, dir
        map[y][x] = directions[dir][2]
        x, y, dir = nextx, nexty, nextdir

    return x, y, dir


def simulate(map, path, use3d = False):
    x = next(i for i, c in enumerate(map[0]) if c != " ")
    y = 0
    d = 0

    for c in path:
        if c == "R":
            d = (d + 1) % 4
        elif c == "L":
            d = (d - 1) % 4
        else:
            c = int(c)
            x, y, d = move(map, x, y, d, c, use3d)

    return x, y, d


def part1():
    map,path = parseInput(input)
    x, y, d = simulate(map, path)
    print_map(map, x, y)
    x += 1
    y += 1
    print(f"[Part 1] x:{x}, y:{y}, d:{d} = " + str(1000 * y + 4 * x + d))


def part2():
    map,path = parseInput(input)
    x, y, d = simulate(map, path, True)
    print_map(map, x, y)
    x += 1
    y += 1
    print(f"[Part 2] x:{x}, y:{y}, d:{d} = " + str(1000 * y + 4 * x + d))

part1()
part2()