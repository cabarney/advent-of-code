from os import path

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = open(inputPath, 'r').readline()

print("Day 6: Tuning Trouble (python)")

def findMarker(buff, cnt):
  for idx in range(cnt-1, len(input)):
    b = buff[idx-cnt:idx]
    if len(set(list(b))) == cnt:
      return idx

buffer = memoryview(bytearray(input, "utf-8"))

print(findMarker(buffer, 4))
print(findMarker(buffer, 14))
