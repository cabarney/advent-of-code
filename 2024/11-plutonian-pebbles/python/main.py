from os import path
from collections import defaultdict

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [int(x) for x in open(inputPath, 'r').readline().strip().split()]

print("Day 11: Plutonian Pebbles (python)")

stones = defaultdict(int)
for stone in input:
    stones[stone] = 1

blinks = 0

while blinks < 75:
    changes = defaultdict(int)
    for stone, cnt in stones.items():
        changes[stone] -= cnt
        if stone == 0:
            changes[1] += cnt
            continue
        str_stone = str(stone)
        length, rem = divmod(len(str_stone), 2)
        if rem == 0:
            changes[int(str_stone[:length])] += cnt
            changes[int(str_stone[length:])] += cnt
        else:
            changes[stone * 2024] += cnt
    for stone, cnt in changes.items():
        stones[stone] += cnt
        if stones[stone] == 0:
            stones.pop(stone)
    blinks += 1
    if blinks == 25:
        print(f"Part 1: {sum(stones.values())}")
print(f"Part 2: {sum(stones.values())}")
