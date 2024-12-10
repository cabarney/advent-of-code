import re
from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]
memory = ''.join(input)

mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")

print("Day 3: Mull It Over (python)")

tot = 0

for match in mul_pattern.finditer(memory):
    a = int(match.group(1))
    b = int(match.group(2))
    tot += a * b

print(f"Total: {tot}")

print("Part 2")
tot = 0

for match in mul_pattern.finditer(memory):
    last_do_index = memory.rfind("do()", 0, match.start())
    last_dont_index = memory.rfind("don't()", 0, match.start())
    if last_dont_index > last_do_index:
        continue
    a = int(match.group(1))
    b = int(match.group(2))
    tot += a * b

print(f"Total: {tot}")