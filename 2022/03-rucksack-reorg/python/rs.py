from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))

print("Day 3: Rucksack Reorganization4 (python)")

def itemToPriority(item):
  ascii = ord(item)
  if ascii >= ord('a'):
    return ascii - ord('a') + 1
  else:
    return ascii - ord('A') + 27

def splitGroupBySize(group, size):
  for i in range(0, len(group), size):
    yield group[i:i + size]

def splitInToGroups(group, n):
  size = int(len(group)/n)
  return splitGroupBySize(group, size)

def findSharedItemPriority(group):
  for item in group[0]:
    if all((item in sack) for sack in group[1:]):
      return itemToPriority(item)

input = [line.strip() for line in (open(inputPath, 'r').readlines())]

prioritySum = sum(findSharedItemPriority(list(splitInToGroups(line, 2))) for line in input)
badgeSum = sum(findSharedItemPriority(group) for group in list(splitGroupBySize(input, 3)))

print("The sum of the mistake items' priorities is", prioritySum)
print("The sum of the group badges is", badgeSum)
