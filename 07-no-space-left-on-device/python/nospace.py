from os import path
import functools

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 7: No Space Left on Device (python)")

class Directory:
  def __init__(self, name, parent) -> None:
    self.name = name
    self.parent = parent
    self.dirs: list[Directory] = []
    self.files: list[tuple[int, str]] = []
    self.size = 0

root = Directory("/", None)
current = root

def processCommand(current: Directory, cmd):
  if cmd[:2] == "cd":
    dir = cmd[3:]
    if dir == "/":
      current = root
    elif dir == "..":
      current = current.parent
    else:
      current = next(x for x in current.dirs if x.name == dir)
  return current

def addFile(dir, file):
  (size, _) = file
  dir.files.append(file)
  while dir != None:
    dir.size += size
    dir = dir.parent

def processOutput(current: Directory, output: str):
  o = output.split(" ")
  if o[0] == "dir":
    current.dirs.append(Directory(o[1], current))
  else:
    addFile(current, (int(o[0]), o[1]))
  return current

def printDir(dir: Directory, indent):
  print(indent * ' ' + "-", dir.name, "(dir, size=" + str(dir.size) + ")")
  for d in dir.dirs:
    printDir(d, indent + 2)
  for f in dir.files:
    print(indent * ' ' + "-", f[1], "(file, size=" + str(f[0]) + ")" )


def findDirs(dir: Directory, predicate) -> list[Directory]:
  dirs = []
  if predicate(dir):
    dirs.append(dir)
  for sd in dir.dirs:
    for d in findDirs(sd, predicate):
      dirs.append(d)  
  return dirs

for line in input:
  if line[0] == '$':
    current = processCommand(current, line[2:])
  else:
    current = processOutput(current, line)


printDir(root, 0)
print("Total size under 100000:", sum([dir.size for dir in findDirs(root, lambda d: d.size <= 100000)]))
spaceNeeded = 30000000 - (70000000 - root.size)
candidates = findDirs(root, lambda d: d.size >= spaceNeeded)
candidates.sort(key = lambda x: x.size)
dir = candidates[0]
print("We should delete the " + dir.name + " directory (size: " + str(dir.size) + ")")