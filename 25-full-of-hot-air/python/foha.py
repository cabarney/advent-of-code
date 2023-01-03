from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 25: Full of Hot Air (python)")

def snafu_to_decimal(snafu):
    dec = 0
    for i, digit in enumerate(snafu[::-1]):
        if digit == "-":
            val = -1
        elif digit == "=":
            val = -2
        else:
            val = int(digit)
        dec += val * 5**i
    return dec

def decimal_to_snafu(dec):
    places = 0
    while x:=5**places <= dec:
        places += 1
    
    snafu = ""
    for i in range(places-1, -1, -1):
        val = dec / 5**i
        if val > 1.5:
            val = 2
            snafu += "2"
        elif val > 0.5:
            val = 1
            snafu += "1"
        elif val > -0.5:
            val = 0
            snafu += "0"
        elif val > -1.5:
            val = -1
            snafu += "-"
        else:
            val = -2
            snafu += "="
        dec -= val * 5**i

    return snafu


total = 0
for line in input:
    total += snafu_to_decimal(line)
print(total)

print("Part 1:", decimal_to_snafu(total))