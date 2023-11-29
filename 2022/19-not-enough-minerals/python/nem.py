from os import path
from collections import deque, namedtuple
import re

basepath = path.dirname(__file__)
# inputPath = path.abspath(path.join(basepath, "..", "ex.txt"))
inputPath = path.abspath(path.join(basepath, "..", "input.txt"))
input = [line.strip() for line in open(inputPath, 'r').readlines()]

print("Day 19: Not Enough Minerals (python)")

Blueprint = namedtuple("Blueprint", ["id", "robot_ore_cost", "clay_ore_cost",
                       "obsidian_ore_cost", "obsidian_clay_cost", "geode_ore_cost", "geode_obsidian_cost"])

State = namedtuple("State", ["time", "robots", "resources"])

pattern = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."


def parseBlueprints(input):
    for line in input:
        match = re.match(pattern, line)
        if match:
            blueprint = Blueprint(*[int(m) for m in match.groups()])
            yield blueprint


blueprints = list(parseBlueprints(input))

def getChoices(blueprint, resources):
    if resources["ore"] >= blueprint.robot_ore_cost:
        yield "ore"
    if resources["ore"] >= blueprint.clay_ore_cost:
        yield "clay"
    if resources["ore"] >= blueprint.obsidian_ore_cost and resources["clay"] >= blueprint.obsidian_clay_cost:
        yield "obsidian"
    if resources["ore"] >= blueprint.geode_ore_cost and resources["obsidian"] >= blueprint.geode_obsidian_cost:
        yield "geode"
    yield "none"

def simulate(blueprint, minutes):
    # blueprint = blueprints[id]
    maxGeodes = 0
    initialState = State(1, {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}, {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0})
    queue = deque([initialState])
    prevTime = 0
    while queue:
        state = queue.popleft()
        if state.time > prevTime:
            print(f"{blueprint.id}, minute {state.time}")
            prevTime = state.time

        if state.time > minutes:
            # p = maxGeodes
            maxGeodes = max(maxGeodes, state.resources["geode"])
            # if maxGeodes > p: print(maxGeodes)
            continue
        
        choices = list(getChoices(blueprint, state.resources))
        if state.time == 24:
            choices = ["none"]
        elif "geode" in choices:
            choices = ["geode"]
        elif "obsidian" in choices and state.robots["obsidian"] < 1:
            choices = ["obsidian"]
        elif "clay" in choices and state.robots["clay"] < 1:
            choices = ["clay"]

        for choice in choices:        
            robots = state.robots.copy()
            resources = state.resources.copy()
            if choice == "ore":
                resources["ore"] -= blueprint.robot_ore_cost
            elif choice == "clay":
                resources["ore"] -= blueprint.clay_ore_cost
            elif choice == "obsidian":
                resources["ore"] -= blueprint.obsidian_ore_cost
                resources["clay"] -= blueprint.obsidian_clay_cost
            elif choice == "geode":
                resources["ore"] -= blueprint.geode_ore_cost
                resources["obsidian"] -= blueprint.geode_obsidian_cost

            for rt in resources:
                resources[rt] += robots[rt]

            if choice != "none":
                robots[choice] += 1

            newState = State(state.time + 1, robots, resources)

            queue.append(newState)
    print(blueprint.id, maxGeodes, blueprint.id * maxGeodes)
    return (blueprint.id, maxGeodes, blueprint.id * maxGeodes)


results = [simulate(blueprint, 24) for blueprint in blueprints]
for r in results:
    print(f"Blueprint {r[0]}: {r[1]} geodes opened, quality level = {r[2]}")
print("Part 1: Max Quality: ", max([r[2] for r in results]))
