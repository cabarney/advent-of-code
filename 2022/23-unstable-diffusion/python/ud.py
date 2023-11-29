from collections import deque, namedtuple, Counter
from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 23: Unstable Diffusion (python)")

Position = namedtuple('Position', ['x', 'y'])

N = Position(0, -1)
NE = Position(1, -1)
E = Position(1, 0)
SE = Position(1, 1)
S = Position(0, 1)
SW = Position(-1, 1)
W = Position(-1, 0)
NW = Position(-1, -1)

all_directions = [N, NE, E, SE, S, SW, W, NW]

all_N_mask = 0b10000011
all_S_mask = 0b00111000
all_W_mask = 0b11100000
all_E_mask = 0b00001110

def pos(elf, dir):
    return Position(elf.x + dir.x, elf.y + dir.y)

def available_pos(elf, elves):
    surrounding = 0b00000000
    for d in range(8):
        if pos(elf, all_directions[d]) in elves:
            surrounding |= 1 << d
    return surrounding

directions = deque([[N, NW, NE],
                    [S, SW, SE],
                    [W, NW, SW], 
                    [E, NE, SE]])

directions_order = deque([(N, all_N_mask), (S, all_S_mask), (W, all_W_mask), (E, all_E_mask)])


def print_elves_and_count_space(elves):
    count = 0
    min_y = min(elves, key=lambda e: e.y).y
    max_y = max(elves, key=lambda e: e.y).y
    min_x = min(elves, key=lambda e: e.x).x
    max_x = max(elves, key=lambda e: e.x).x
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in elves:
                print('#', end='')
            else:
                print('.', end='')
                count += 1
        print()
    print()
    print()
    return count

def parse_input(input):
    for r, row in enumerate(input):
        for c in (i for i, x in enumerate(row) if x == '#'):
            yield Position(c, r)


def simulate(end_condition):
    elves = set(parse_input(input))
    turn = 0
    move_cnt = 1
    while not end_condition(turn, move_cnt):
        elf_positions = dict({elf:available_pos(elf, elves) for elf in elves})
        move_to_positions = dict()
        for elf in elves:
            if elf_positions[elf] == 0:
                move_to_positions[elf] = elf
                continue
            dir = next((dir for dir in directions_order if elf_positions[elf] & dir[1] == 0), None)
            if dir:
                move_to_positions[elf] = pos(elf, dir[0])
            else:
                move_to_positions[elf] = elf
        move_cnt = len([k for k, v in move_to_positions.items() if k != v])
        bad_moves = set(pos for pos, cnt in Counter(move_to_positions.values()).items() if cnt > 1)
        elves = set(move if move not in bad_moves else curr for curr, move in move_to_positions.items())
        turn += 1
        directions_order.rotate(-1)
    return turn, print_elves_and_count_space(elves)


print("Part 1:", simulate(lambda turn, _: turn == 10))
print("Part 2:", simulate(lambda _, move_cnt: move_cnt == 0))
