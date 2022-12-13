import math
from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = open(inputPath, 'r').read().split("\n\n")
monkeyInput = [[l.strip() for l in line.splitlines()] for line in input]

print("Day 11: Monkey in the Middle (python)")

class Monkey:
    def __init__(self, lines):
        self.items = [int(item) for item in lines[1].replace("Starting items: ", "").split(", ")]
        opParts = lines[2].split(" ")[-2:]
        if opParts[0] == "+":
            self.opType = "+"
            self.operation = lambda x: x + int(opParts[1])
        elif opParts[0] == "*":
            self.opType = "*"
            self.operation = lambda x: x * (x if opParts[1] == "old" else int(opParts[1]))
        self.testModulo = int(lines[3].split(" ")[-1])
        self.trueMonkey = int(lines[4].split(" ")[-1])
        self.falseMonkey = int(lines[5].split(" ")[-1])
        self.processedItems = 0

    def process(self, worryMod):
        for item in self.items:
            self.processedItems += 1
            item = self.operation(item)
            if worryMod: item //= 3
            if item % self.testModulo == 0:
                yield (self.trueMonkey, item)
            else:
                yield (self.falseMonkey, item)
        self.items = []

    def print(self, idx):
        print("Monkey", idx+1, self.items)


def simulate(rounds, worryMod):
    monkeys = [Monkey(lines) for lines in monkeyInput]
    allModulos = [monkey.testModulo for monkey in monkeys]
    lcm = allModulos[0]
    for i in range(1, len(allModulos)):
        lcm = lcm * allModulos[i] // math.gcd(lcm, allModulos[i])

    for i in range(rounds):
        for monkey in monkeys:
            for op in monkey.process(worryMod):
                monkeys[op[0]].items.append(op[1] % lcm)

    top = sorted([monkey.processedItems for monkey in monkeys], reverse=True)[:2]
    print(rounds, "Rounds", "with" if worryMod else "without", "worry modification:", top[0] * top[1])

for params in [(20, True), (10000, False)]:
    simulate(*params)
