from os import path
import copy

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line[:-1] for line in open(inputPath, 'r').readlines()]

print("Day 5: Supply Stacks (python)")

configLines = []
for line in input:
  if line == "":
    break
  configLines.append(line)

commands = input[len(configLines)+1:]

def initializeStacks():
  stacks = [[],[],[],[],[],[],[],[],[]]
  configLines.reverse()
  for line in configLines[1:]:
    for stack in range(9):
      idx = stack * 4 + 1
      if line[idx] != " ":
        stacks[stack].append(line[idx])
  return stacks

def parseCommand(command):
  command = command.strip()
  command = command.replace("move ", "")
  command = command.replace(" from ", ",")
  command = command.replace(" to ", ",")
  parts = command.split(",")
  return (int(parts[0]), int(parts[1]) - 1, int(parts[2]) - 1)

def crateMover9000(inputStacks):
  stacks = copy.deepcopy(inputStacks)
  for line in commands:
    command = parseCommand(line)
    for _ in range(command[0]):
      stacks[command[2]].append(stacks[command[1]].pop())
  return stacks

def crateMover9001(inputStacks):
  stacks = copy.deepcopy(inputStacks)
  for line in commands:
    command = parseCommand(line)
    move = []
    for _ in range(command[0]):
      move.append(stacks[command[1]].pop())
    for _ in range(command[0]):
      stacks[command[2]].append(move.pop())
  return stacks

def displayResult(stacks, scenario):
  result = ""
  for i in range(9):
    result += stacks[i][-1]
  print(scenario, ": ", result)

stacks = initializeStacks()

cm9000 = crateMover9000(stacks)
cm9001 = crateMover9001(stacks)

displayResult(cm9000, "CrateMover 9000")
displayResult(cm9001, "CrateMover 9001")
