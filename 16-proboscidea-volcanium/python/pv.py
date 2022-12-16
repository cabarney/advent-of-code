from collections import deque, namedtuple
from copy import copy
from enum import Enum
from os import path
import re

basepath = path.dirname(__file__)
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]
INF = int(1e9)

Valve = namedtuple("Valve", ["id", "flow", "tunnels"])

print("Day 16: Proboscidea Valcanium (python)")

def parseInput(input):
    valves = {}
    for line in input:
        match = re.search(r"Valve (\w+) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? (.*)", line)
        if match:
            id, flow, tunnels = match.groups()
            valves[id] = Valve(id.strip(), int(flow), [t.strip() for t in tunnels.split(",")])
    return valves

def floid_warshall(valves):
    dist = {v: {u: INF for u in valves} for v in valves}
 
    for v in valves:
        dist[v][v] = 0
        for u in valves[v].tunnels:
            dist[v][u] = 1
 
    for k in valves:
        for i in valves:
            for j in valves:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
 
    return dist

def generate_open_options(pos, open_valves, time_left):
    for next in nonZeroValves:
        if next not in open_valves and distances[pos][next] < time_left:
            open_valves.append(next)
            yield from generate_open_options(
                next, open_valves, time_left - distances[pos][next] - 1
            )
            open_valves.pop()

    yield copy(open_valves)

def get_order_score(open_order, time_left):
    now, ans = "AA", 0
    for pos in open_order:
        time_left -= distances[now][pos] + 1
        ans += valves[pos].flow * time_left
        now = pos
    return ans

valves = parseInput(input)
distances = floid_warshall(valves)
nonZeroValves = [v for v in valves if valves[v].flow > 0]

options = generate_open_options("AA", [], 30)
scores = [get_order_score(o, 30) for o in options]
print("Part 1:", max(scores))

options = list(generate_open_options("AA", [], 26))
best_scores = {}

for order in options:
    tup = tuple(sorted(order))
    score = get_order_score(order, 26)
    best_scores[tup] = max(best_scores.get(tup, 0), score)

best_scores = list(best_scores.items())

max_score = 0
for human in range(len(best_scores)):
    for elephant in range(human + 1, len(best_scores)):
        human_opens, human_score = best_scores[human]
        elephant_opens, elephant_score = best_scores[elephant]

        if len(set(human_opens).intersection(set(elephant_opens))) == 0:
            max_score = max(max_score, human_score + elephant_score)

print("Part 2:", max_score)