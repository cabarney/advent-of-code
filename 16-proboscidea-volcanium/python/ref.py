from os import path
import re
from collections import deque


def bfs(tunnels, start, targets):
    dist = {start: 0}
    seen = {start}
    q = deque([start])
    while q and any(t not in dist for t in targets):
        p = q.popleft()
        for x in tunnels[p]:
            if x not in seen:
                seen.add(x)
                dist[x] = dist[p] + 1
                q.append(x)
    return dist


def find_paths(dist, rates, t):
    pressures = []
    paths = []
    stack = [(t, 0, ['AA'])]
    while stack:
        t, p, path = stack.pop()
        cur = path[-1]
        new = []
        for n, d in dist[cur].items():
            if d > t - 2 or n in path:
                continue
            tt = t - d - 1
            pp = p + rates[n] * tt
            s = tt, pp, path + [n]
            new.append(s)
        if new:
            stack.extend(new)
        else:
            pressures.append(p)
            # paths always start at AA, so no need to keep first location
            paths.append(path[1:])
    return pressures, paths


def solve(data: str):
    rates = {}
    tunnels = {}
    for line in data.splitlines():
        match = re.search(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line)
        if match:
            valve, r, t = match.groups()
            rates[valve] = int(r)
            tunnels[valve] = [x.strip() for x in t.split(',')]

    # Part One
    dist = {}
    for start in ('AA', *rates):
        dist[start] = {}
        d = bfs(tunnels, start, rates)
        for r in rates:
            if r != start and r in d:
                dist[start][r] = d[r]

    p, _ = find_paths(dist, rates, 30)
    print(max(p))

    # # Part Two
    # x = list(zip(*find_paths(dist, rates, 26)))
    # p, paths = zip(*sorted(x, reverse=True))
    # i, j = 0, 1
    # while any(x in paths[j] for x in paths[i]):
    #     j += 1
    # ans = p[i] + p[j]  # lower bound
    # j_max = j  # since p[i] can only decrease, j cannot exceed this
    # for i in range(1, j_max):
    #     for j in range(i + 1, j_max + 1):
    #         if any(x in paths[j] for x in paths[i]):
    #             continue
    #         ans = max(ans, p[i] + p[j])
    # print(ans)


if __name__ == '__main__':
    basepath = path.dirname(__file__)
    inputPath = path.abspath(path.join(basepath, "..", "ex.txt"))
    input = open(inputPath, 'r').read()
    solve(input)
