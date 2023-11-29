from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 10: Cathode Ray Tube (python)")

interestingCycles = [20, 60, 100, 140, 180, 220]
x = 1
cycle = 1
interestingCycleTotal = 0
screen = []

def incrementCycle():
    global cycle, interestingCycleTotal, screen
    if cycle in interestingCycles:
        interestingCycleTotal += (x * cycle)
    screen.append("#" if (cycle-1) % 40 in [x-1, x, x+1] else ".")
    cycle += 1

for line in input:
    if line == "noop":
        incrementCycle()
        continue
    dx = int(line.split(" ")[1])
    incrementCycle()
    incrementCycle()
    x += dx

print(interestingCycleTotal)
for i in range(6):
    print("".join(screen[i*40:(i+1)*40]))