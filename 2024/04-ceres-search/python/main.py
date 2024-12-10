from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 4: Ceres Search (python)")

directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
    'UL': (-1, -1),
    'UR': (1, -1),
    'DL': (-1, 1),
    'DR': (1, 1)
}

is_xmas = [['.' for _ in line] for line in input]

def print_grid():
    for line in is_xmas:
        print(''.join(line))

def get_directional_word(x, y, dir):
    word = ''
    (dx, dy) = directions[dir]
    if x + 3 * dx < 0 or x + 3 * dx >= len(input):
        return word
    if y + 3 * dy < 0 or y + 3 * dy >= len(input[0]):
        return word
    for i in range(4):
        word += input[x + i * dx][y + i * dy]
    if word == 'XMAS':
        for i in range(4):
            is_xmas[x + i * dx][y + i * dy] = input[x + i * dx][y + i * dy]
    return word

def xmas_cnt(x, y):
    xmas_cnt = 0
    for dir in directions:
        if get_directional_word(x, y, dir) == 'XMAS':
            xmas_cnt += 1
    return xmas_cnt

cnt = sum(xmas_cnt(x, y) for x, line in enumerate(input) for y, c in enumerate(line) if c == 'X')
print(f"Count: {cnt}")
# print_grid()


def is_x_mas(x, y):
    if x < 1 or y < 1 or x > len(input) - 2 or y > len(input[0]) - 2:
        return False
    if input[x][y] != 'A':
        return False
    ul_dr = input[x - 1][y - 1] + input[x + 1][y + 1]
    ur_dl = input[x - 1][y + 1] + input[x + 1][y - 1]
    if ul_dr in ('SM', 'MS') and ur_dl in ('SM', 'MS'):
        return True


print("Part 2")
cnt = sum(1 for x, line in enumerate(input) for y, _ in enumerate(line) if is_x_mas(x, y))
print(f"Count: {cnt}")
