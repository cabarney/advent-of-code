from collections import namedtuple
from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

Monkey = namedtuple("Monkey", ["name", "value", "left", "op", "right"])

print("Day 21: Monkey Math (python)")

def parseLine(line):
    parts = line.split(":")
    name = parts[0]
    job = parts[1].strip().split(" ",)
    if len(job) == 1:
        return Monkey(name, int(job[0]), None, None, None)
    return Monkey(name, None, *job)

def upt(monkey, field, value):
    if field == "left":
        return Monkey(monkey.name, monkey.value, value, monkey.op, monkey.right)
    if field == "right":
        return Monkey(monkey.name, monkey.value, monkey.left, monkey.op, value)
    if field == "op":
        return Monkey(monkey.name, monkey.value, monkey.left, value, monkey.right)
    if field == "value":
        return Monkey(monkey.name, value, monkey.left, monkey.op, monkey.right)
    return monkey

def run(pt2 = False):
    monkeys = {monkey.name: monkey for monkey in [parseLine(line) for line in input]}
    valueMonkeys = {monkey.name: monkey.value for monkey in monkeys.values() if monkey.value is not None}
    monkeys = {monkey.name: monkey for monkey in monkeys.values() if monkey.name not in valueMonkeys}

    if pt2:
        valueMonkeys = dict(filter(lambda x: x[0] != "humn", valueMonkeys.items()))
        root = monkeys["root"]
        monkeys["root"] = Monkey(root.name, root.value, root.left, "=", root.right)

    while "root" not in valueMonkeys:
        for name, value in valueMonkeys.items():
            for monkey in (m for m in monkeys.values() if m.left == name or m.right == name):
                if monkey.left == name:
                    monkey = upt(monkey, "left", value)
                if monkey.right == name:
                    monkey = upt(monkey, "right", value)
                if type(monkey.left) == int and type(monkey.right) == int:
                    if monkey.op == "+":
                        monkey = upt(monkey, "value", monkey.left + monkey.right)
                    elif monkey.op == "-":
                        monkey = upt(monkey, "value", monkey.left - monkey.right)
                    elif monkey.op == "*":
                        monkey = upt(monkey, "value", monkey.left * monkey.right)
                    elif monkey.op == "/":
                        monkey = upt(monkey, "value", monkey.left // monkey.right)
                monkeys[monkey.name] = monkey
            
        newValueMonkeys = [m for m in monkeys.values() if m[1] is not None]
        for monkey in newValueMonkeys:
            valueMonkeys[monkey.name] = monkey[1]
        monkeys = {monkey.name: monkey for monkey in monkeys.values() if monkey.name not in valueMonkeys}

        if pt2 and len(newValueMonkeys) == 0:
            if any(type(value) == int for value in [monkeys["root"].left, monkeys["root"].right]):
                valueMonkeys["root"] = monkeys["root"]
    
    if not pt2:
        return valueMonkeys["root"]
    
    def get(monkey, t):
        return monkey.left if type(monkey.left) == t else monkey.right

    root = monkeys["root"]
    target = get(root, int)
    nextUnknown = get(root, str)
    while True:
        if nextUnknown == "humn":
            return target
        monkey = monkeys[nextUnknown]
        if monkey.op == "+":
            target = target - get(monkey, int)
        elif monkey.op == "-":
            if type(monkey.left) == int:
                target = monkey.left - target
            else:
                target = target + monkey.right
        if monkey.op == "*":
            target = target // get(monkey, int)
        elif monkey.op == "/":
            if type(monkey.left) == int:
                target = monkey.left // target
            else:
                target = monkey.right * target
        nextUnknown = get(monkey, str)
            

print("Part 1:", run())
print("Part 2:", run(True))