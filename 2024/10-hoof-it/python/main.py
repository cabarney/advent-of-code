from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [[int(x) for x in line.strip()] for line in open(inputPath, 'r').readlines()]

print("Day 10: Hoof It (python)")

def input_val(x, y):
    if y < 0 or y >= len(input) or x < 0 or x >= len(input[0]):
        return None
    return input[y][x]

def find_value_locations(value):
    locations = []
    for y, row in enumerate(input):
        for x, val in enumerate(row):
            if val == value:
                locations.append((x, y))
    return locations

paths_to_peaks = [[[] for _ in row] for row in input]
peaks = find_value_locations(9)
for peak in peaks:
    paths_to_peaks[peak[1]][peak[0]].append(peak)
for h in range(9, 0, -1):
    locations = find_value_locations(h)
    for loc in locations:
        x, y = loc
        surrounds = [(_x, _y) for _x, _y in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)] if input_val(_x, _y) == h - 1]
        for point in surrounds:
            paths_to_peaks[point[1]][point[0]].extend(paths_to_peaks[y][x])

print(f"Part 1: {sum(len(set(paths_to_peaks[y][x])) for x, y in find_value_locations(0))}")
print(f"Part 2: {sum(len(paths_to_peaks[y][x]) for x, y in find_value_locations(0))}")
