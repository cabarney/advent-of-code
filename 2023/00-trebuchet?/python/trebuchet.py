from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

digitMappings = [
    ['one', '1'],
    ['two', '2'],
    ['three', '3'],
    ['four', '4'],
    ['five', '5'],
    ['six', '6'],
    ['seven', '7'],
    ['eight', '8'],
    ['nine', '9']
]

def parseLine(line, useDigitStringReplacement = False):
    line = line.strip()
    parsed = ''

    for i in range(0, len(line)):
        if line[i].isdigit():
            parsed += line[i]
        if not useDigitStringReplacement:
            continue
        for map in digitMappings:
            if line[i:].startswith(map[0]):
                parsed += map[1]    

    return parsed

def calcCalibrationValue(lines):
    return sum(int(line[0] + line[-1]) for line in lines)

print("Day 0: Trebuchet? (python)")

part1input = [parseLine(line) for line in input]
print(f'Part 1: {calcCalibrationValue(part1input)}')


part2input = [parseLine(line, True) for line in input]
print(f'Part 2: {calcCalibrationValue(part2input)}')