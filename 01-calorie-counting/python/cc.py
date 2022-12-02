from os import path
basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))

print("Day 1: Calorie Counting (python)")

input = open(inputPath, 'r').readlines()
elves = [[int(cal) for cal in group.split("\n")] for group in "".join(input).split("\n\n")]
elves = sorted([sum(elf) for elf in elves], reverse=True)

print("The elf with the most calories has", elves[0])
print("The top 3 elves are carrying a total of", sum(elves[:3]), "calories")


# SECOND ATTEMPT
# import itertools as it

# with open('../input.txt') as f:
#   data = [i for i in f.read().strip().split("\n")]
# grouped = it.groupby(data, lambda x: x == "")

# elves = sorted(list(sum(list(int(c) for c in calories)) for match, calories in grouped if not match), reverse=True)
# print("The elf with the most calories is", elves[0])
# print("The top 3 elves are carrying a total of", sum(elves[:3]), "calories")


# FIRST ATTEMPT

# elves = dict()
# idx = 0
# calories = 0

# lines = open("../input.txt", "r").readlines()
# for line in lines:
#   line = line.strip()
#   if line == "":
#     elves[idx] = calories
#     idx += 1
#     calories = 0
#     continue
#   calories += int(line)

# elves[idx] = calories

# part 1
# m = max(elves.values())
# e = max(elves, key=elves.get) + 1

# print("Elf {} has {} calories".format(e, m))

# part 2
# top = sum(sorted(elves.values(), reverse=True)[:3])
# print("Top 3 elves have {} calories".format(top))

