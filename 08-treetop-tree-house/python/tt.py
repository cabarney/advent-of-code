from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 8: Treetop Tree House (python)")

grid = [[int(val) for val in line] for line in input]

def printTrees():
  BLUE = '\033[94m'
  END = '\033[0m'
  for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
      t = grid[y][x]
      if isVisible(t, x, y):
        print(f"{BLUE}{t}{END}", end='')
      else:
        print(t, end='')
    print()

def isVisible(t, x, y):
  if x == 0 or x == len(grid[0]) or y == 0 or y == len(grid):
    return True
  
  vl = all(grid[y][i] < t for i in range(0, x))
  vr = all(grid[y][i] < t for i in range(x+1, len(grid[y])))
  vu = all(grid[i][x] < t for i in range(0, y))
  vd = all(grid[i][x] < t for i in range(y+1, len(grid)))

  return any([vl, vr, vu, vd])

def cntToNext(trees, height, rev=False):
  if not trees: return 0
  if rev: trees.reverse()
  for i in range(0, len(trees)):
    if trees[i] >= height:
      return i + 1
  return len(trees)

def treesInView(t, x, y):
  l = cntToNext(grid[y][0:x], t, True)
  r = cntToNext(grid[y][x+1:], t)
  u = cntToNext([grid[i][x] for i in range(0, y)], t, True)
  d = cntToNext([grid[i][x] for i in range(y+1,len(grid))], t)
  return l * r * u * d

print("The number of visible trees is", sum(isVisible(grid[y][x], x, y) for x in range(len(grid[0])) for y in range(len(grid))))
print("The most scenic tree can see", max(treesInView(grid[y][x], x, y) for x in range(len(grid[0])) for y in range(len(grid))), "trees")
