from os import path
import concurrent.futures

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

def get_input_copy(obstacle_location = None):
    grid = [f"o{line}o" for line in input]
    grid.insert(0, "o" * len(grid[0]))
    grid.append("o" * len(grid[0]))
    if obstacle_location:
        x, y = obstacle_location
        # x += 1
        # y += 1
        grid[y] = grid[y][:x] + '#' + grid[y][x + 1:]
    return grid

print("Day 6: Guard Gallivant (python)")

def get_val(grid, pos):
    return grid[pos[1]][pos[0]]


def find_cursor(grid, d):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == d:
                return (x, y)
    return (0, 0)

move_offsets = [(0, -1),(1, 0),(0, 1),(-1, 0)]

def print_grid(grid):
    for line in grid:
        print(line)
    print()

def print_enhanced_grid(grid, points, c):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if (x, y) in points:
                print(c, end='')
            else:
                print(char, end='')
        print()
    print()

def move_next(grid, d, cur):
    offset = move_offsets[d]
    next = (cur[0] + offset[0], cur[1] + offset[1])
    val = get_val(grid, next)
    if val == '#':
        d = (d + 1) % 4
        return (d, cur, val)
    return (d, next, val)


def patrol(grid):
    d = 0
    cur = find_cursor(grid, '^')
    loop = False
    visited = [(cur, d)]
    while True:
        d, cur, val = move_next(grid, d, cur)
        if (cur, d) in visited:
            loop = True
            break
        elif val == 'o':
            break
        else:
            visited.append((cur, d))
    return (set([pos for pos, _ in visited]), loop)

traveled = patrol(get_input_copy())
print_enhanced_grid(get_input_copy(), traveled[0], 'X')

print ("  Part 1:", len(traveled[0]))

def check_for_loop(pos):
    grid = get_input_copy(pos)
    return patrol(grid)[1]

def part2(path_points):
    looping_obstacles = []
    for i, pos in enumerate(path_points):
        if check_for_loop(pos):
            looping_obstacles.append(pos)
        if i % 10 == 0:
            print(f"Checking {i}/{len(path_points)} ({len(looping_obstacles)} so far)")
    print("  Part 2:", len(looping_obstacles))
    print_enhanced_grid(get_input_copy(), looping_obstacles, '0')

orig_pos = find_cursor(get_input_copy(), '^')
traveled[0].remove(orig_pos)
part2(traveled[0])