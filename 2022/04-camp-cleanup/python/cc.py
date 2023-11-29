from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 4: Camp Cleanup (python)")

def fullyOverlaps(r1, r2):
  (r1a,r1b) = r1.split('-')
  (r2a,r2b) = r2.split('-')
  (r1a, r1b, r2a, r2b) = (int(r1a), int(r1b), int(r2a), int(r2b))
  return (r1a <= r2a and r1b >= r2b) or (r2a <= r1a and r2b >= r1b)

def partiallyOverlaps(r1, r2):
  (r1a, r1b) = r1.split('-')
  (r2a, r2b) = r2.split('-')
  (r1a, r1b, r2a, r2b) = (int(r1a), int(r1b), int(r2a), int(r2b))
  return (r1a >= r2a and r1a <= r2b) or (r1b >= r2a and r1b <= r2b) or (r2a >= r1a and r2a <= r1b) or (r2b >= r1a and r2b <= r1b)

def splitPairs(line):
  return line.split(',')

input = [splitPairs(line) for line in input]

fullyOverlapping = list(filter(lambda x: fullyOverlaps(x[0], x[1]), input))
print("The number of pairs where one range fully contains the other is", len(fullyOverlapping))

partiallyOverlapping = list(filter(lambda x: partiallyOverlaps(x[0], x[1]), input))
print("The number of pairs where one range overlaps the other is", len(partiallyOverlapping))

