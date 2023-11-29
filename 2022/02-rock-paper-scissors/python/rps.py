from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))

print("Day 2: Rock, Paper, Scissors (python)")

def simulateHands(part: int, scoring: dict):
  total = sum(scoring[hand] for hand in input)
  print(f"The Part {part} total score is", total)

input = open(inputPath, 'r').readlines()
input = [line.strip().replace(' ', '') for line in input]

simulateHands(1, { 'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6 })
simulateHands(2, { 'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7 })
