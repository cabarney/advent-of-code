from collections import deque, namedtuple
from ctypes import c_int8
from os import path
from array import array
import time

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = deque(list(open(inputPath, 'r').read().strip()))
# input = deque(list(">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"))
Shape = namedtuple("Shape", ["w", "h", "data"])
Position = namedtuple("Position", ["x", "y"])

print("Day 17: Pyroclastic Flow (python)")

shapes = [[[1, 1, 1, 1]], [[0, 1, 0], [1, 1, 1], [0, 1, 0]], [[1, 1, 1],[0, 0, 1], [0, 0, 1]], [[1], [1], [1], [1]], [[1, 1], [1, 1]]]
shapes2 = [Shape(4,1,[0b1111]), Shape(3,3,[0b010,0b111,0b010]), Shape(3,3,[0b111,0b001,0b001]), Shape(1,4,[0b1,0b1,0b1,0b1]), Shape(2,2,[0b11,0b11])]
shapes3 = [{Position(0, 0), Position(1, 0), Position(2, 0), Position(3, 0)},
           {Position(0, 1), Position(1, 1), Position(2, 1), Position(1, 0), Position(1, 2)},
           {Position(0, 0), Position(1, 0), Position(2, 0), Position(2, 1), Position(2, 2)},
           {Position(0, 0), Position(0, 1), Position(0, 2), Position(0, 3)},
           {Position(0, 0), Position(1, 0), Position(0, 1), Position(1, 1)}]

def simulate3(total_shapes):
    foo = set()
    top = -1
    full_row = -1
    
    def offset_shape(shape, pos): 
        return {Position(p.x + pos.x, p.y + pos.y) for p in shape}

    def is_valid_position(shape):
        if any([p.x < 0 or p.x >= 7 or p.y < 0 for p in shape]):
            return False
        return not foo.intersection(next_pos)

    def print_grid(shape_data = None):
        for y in range(20, -1, -1):
            print("|", end="")
            for x in range(7):
                if Position(x,y) in foo:
                    print("#", end="")
                elif shape_data is not None and Position(x,y) in shape_data:
                    print("@", end="")
                else: print(".", end="")
            print("|")
        print("+-------")
        print()
        print()



    shape_cnt = 0
    prev_time = time.time()
    while shape_cnt < total_shapes:
        if shape_cnt % 1000 == 0:
            foo = set(filter(lambda p: p.y > top - 100, foo))
        if shape_cnt % 10000 == 0:
            print(shape_cnt, "->", time.time() - prev_time)
            prev_time = time.time()
        shape = shapes3[shape_cnt % 5]
        pos = Position(2, top + 4)
        stopped = False
        shape_pos = offset_shape(shape, pos)
        while not stopped:
            # print_grid(shape_pos)
            wind = input.popleft()
            input.append(wind)

            next_pos = offset_shape(shape_pos, Position(1, 0) if wind == ">" else Position(-1, 0))
            
            if (is_valid_position(next_pos)):
                shape_pos = next_pos
            next_pos = offset_shape(shape_pos, Position(0, -1))
            if (is_valid_position(next_pos)):
                shape_pos = next_pos
            else:
                stopped = True
                foo = foo.union(shape_pos)
                top = max(top, *[p.y for p in shape_pos])
        shape_cnt += 1
    # print_grid()
    return top + 1

        
def simulate2(total_shapes):
    def is_valid_position(shape: Shape, pos):
        if pos.x < 0 or pos.x + shape.w > 7 or pos.y < 0:
            return False
        x = mv[pos.y:pos.y+shape.h]
        if x[0] == 0: return True
        for i in range(shape.h):
            if shape.data[i] << pos.x & x[i]:
                return False
        return True
        # return not any(shape.data[i] << pos.x & grid[pos.y + i] for i in range(shape.h))

    def apply_shape(shape, pos):
        for i in range(shape.h):
            mv[pos.y + i] = mv[pos.y + i] | (shape.data[i] << pos.x)
    
    def get_top():
        for i in range(len(grid) -1, -1, -1):
            if mv[i] > 0: return i
        return -1

    def find_full_row():
        for i in range(len(grid)-1, -1, -1):
            if mv[i] == 0b1111111: return i
        return 0

    def print_grid(shape = None, pos = None):
        def in_shape(x, y):
            if shape is not None and pos is not None:
                shape_x, shape_y = x - pos.x, y - pos.y
                if shape_y >= 0 and shape_y < shape.h and shape_x >= 0 and shape_x < shape.w:
                    return shape.data[shape_y] & 1 << shape_x
            return False

        for y in range(len(grid) -1, -1, -1):
            print(str(y).rjust(5), "|", end="")
            line = ""
            for x in range(7):
                if in_shape(x, y): 
                    line += "@"
                    # print("@", end="")
                else:
                    line += "#" if 1 << x & grid[y] else "."
                    # print("#" if 1 << x & grid[y] else ".", end="")

            print(line[::-1], "|", sep="")
        print("      +-------+")
        print()
        print()

    grid = array("h")
    mv = memoryview(grid)
    shape_cnt = 0
    offset = 0

    prev_time = time.time()
    while shape_cnt < total_shapes:
        if shape_cnt % 10000 == 0:
            print(shape_cnt, "->", time.time() - prev_time)
            prev_time = time.time()
        full_row = find_full_row()
        if full_row > 0:
            offset += full_row
            grid = grid[full_row:]
        shape = shapes2[shape_cnt % 5]
        top = get_top()
        pos = Position(5-shape.w, top + 4)
        while(len(grid) < pos.y + shape.h):
            grid.append(0)
        
        stopped = False
        # print_grid(shape, pos)
        while not stopped:
            # print_grid(shape, pos)
            wind_dir = input.popleft()
            input.append(wind_dir)
            next_pos = Position(pos.x - 1, pos.y) if wind_dir == ">" else Position(pos.x + 1, pos.y)
            if is_valid_position(shape, next_pos):
                pos = next_pos
            
            next_pos = Position(pos.x, pos.y - 1)
            if is_valid_position(shape, next_pos):
                pos = next_pos
            else:
                apply_shape(shape, pos)
                stopped = True                    
        
        shape_cnt += 1
        
    
    return get_top() + offset + 1

def simulate(total_shapes):
    def is_valid_position(shape, pos):
        if pos[0] < 0 or pos[0] + len(shape[0]) > 7 or pos[1] < 0:
            return False
        for r in range(len(shape)):
            for c in range(len(shape[0])):
                if shape[r][c] == 1 and grid[pos[1] - r][pos[0] + c] == 1:
                    return False
        return True


    def apply_shape(shape, pos):
        for r in range(len(shape)):
            for c in range(len(shape[0])):
                if shape[r][c] == 1:
                    grid[pos[1] - r][pos[0] + c] = 1


    def printGrid(shape=None, pos=None):
        def is_in_shape(r, c):
            if shape is None or pos is None:
                return False
            shape_r, shape_c = pos[1] - r, c - pos[0]
            if shape_r < 0 or shape_r >= len(shape) or shape_c < 0 or shape_c >= len(shape[0]):
                return False
            return shape[shape_r][shape_c] == 1
        for r in range(len(grid) - 1, -1, -1):
            print("|", end="")
            row = grid[r]
            for c in range(len(row)):
                if is_in_shape(r, c):
                    print("@", end="")
                else:
                    print("#" if grid[r][c] else ".", end="")
            print("|")
        print("+-------+")
        print()


    def get_top():
        for r in range(len(grid) - 1, -1, -1):
            if 1 in grid[r]:
                return r
        return -1


    def find_full_row():
        for r in range(len(grid) - 1, -1, -1):
            if 0 not in grid[r]:
                return r
        return 0


    grid = []    
    shape_cnt = 0
    offset = 0
    prev_time = time.time()
    while shape_cnt < total_shapes:
        if shape_cnt % 10000 == 0:
            print(shape_cnt, "->", time.time() - prev_time)
            prev_time = time.time()
        full_row = find_full_row()
        if full_row > 0:
            offset += full_row
            grid = grid[full_row:]

        shape = shapes[shape_cnt % len(shapes)]
        top = get_top()
        pos = (2, top + 3 + len(shape))
        while len(grid) <= pos[1]:
            grid.append([0] * 7)
        
        stopped = False
        while not stopped:
            # printGrid(shape, pos)
            # Apply Wind
            wind_dir = input.popleft()
            input.append(wind_dir)
            next_pos = (pos[0] + 1, pos[1]) if wind_dir == ">" else (pos[0] - 1, pos[1])
            if is_valid_position(shape, next_pos):
                pos = next_pos
            
            # Apply Gravity
            next_pos = (pos[0], pos[1] - 1)
            if is_valid_position(shape, next_pos):
                pos = next_pos
            else:
                apply_shape(shape, pos)
                stopped = True
        
        shape_cnt += 1

    return offset + get_top() + 1

# print("Part 1:", simulate(2022))
print("Part 1:", simulate(1_000_000_000_000))
# print("Part 1:", simulate2(2022))
# print("Part 1:", simulate2(1_000_000_000_000))
# print("Part 1:", simulate3(2022))
# print("Part 1:", simulate3(1_000_000_000_000))
