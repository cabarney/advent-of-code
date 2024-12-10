from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()][0]

print("Day 9: Disk Defragmenter (python)")

def convert_to_disk(data):
    disk = []
    for i, length in enumerate(data):
        if i % 2 == 0:
            disk.extend([int(i/2) for _ in range(int(length))])
        else:
            disk.extend([None for _ in range(int(length))])
    return disk

def convert_to_file_map(data):
    file_map = []
    for i, length in enumerate(data):
        if i % 2 == 0:
            file_map.append((int(i/2), int(length)))
        else:
            file_map.append((None, int(length)))
    return file_map

def print_disk(disk):
    for item in disk:
        if item is not None:
            print(item, end="")
        else:
            print('.', end="")
    print()

def print_file_map(file_map):
    for item in file_map:
        if item[0] is not None:
            print(str(item[0])*item[1], end="")
        else:
            print('.' * item[1], end="")
    print()

def defragment_by_chunk(disk):
    idx = 0
    chunks = len(disk) - disk.count(None)
    for i in range(len(disk) - 1, chunks - 2, -1):
        # print_disk(disk)
        if disk[i] is None:
            continue
        else:
            while disk[idx] is not None:
                idx += 1
            disk[idx], disk[i] = disk[i], None
    return disk

def defragment_by_file(file_map):
    file_id = max([x[0] for x in file_map if x[0] is not None])

    while file_id >= 1:
        file_idx = next((i for i, item in enumerate(file_map) if item[0] == file_id), None)
        spc_idx = next((i for i, item in enumerate(file_map[:file_idx]) if item[0] is None and item[1] >= file_map[file_idx][1]), None)
        if spc_idx is None:
            file_id -= 1
            continue
        
        spc_length = file_map[spc_idx][1]
        length = file_map[file_idx][1]
        file_map[file_idx] = (None, length)
        if spc_length - length == 0:
            # file_map.pop(spc_idx)
            file_map[spc_idx] = (file_id, length)
        else:
            file_map[spc_idx] = (None, spc_length - length)
            file_map.insert(spc_idx, (file_id, length))
        file_id -= 1

    return file_map

def calc_checksum(file_map):
    tot = 0
    idx = 0
    for file in file_map:
        for _ in range(file[1]):
            tot += idx * file[0] if file[0] is not None else 0
            idx += 1
    return tot 


disk = convert_to_disk(input)
disk = defragment_by_chunk(disk)
checksum = sum([i * x for i, x in enumerate(disk) if x is not None])
print(f"Part 1: {checksum}")

file_map = convert_to_file_map(input)
file_map = defragment_by_file(file_map)
# print_file_map(file_map)
checksum = sum([i * x for i, x in enumerate(disk) if x is not None])
print(f"Part 2: {calc_checksum(file_map)}")