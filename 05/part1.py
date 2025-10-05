from ast import Tuple
from pprint import pprint
import pprint as pp
import re
import json

input_file = open("input/input.txt")
#input_file = open("input/input.txt")
input_lines = input_file.readlines()

global DEBUG
DEBUG=False

class Seed:
    id: int

class AlmanacMapRange:
    destinationRangeStart = -1
    sourceRangeStart = -1
    rangeLength = -1

    def __init__(self, destinationRangeStart: int, sourceRangeStart: int, rangeLength: int):
        self.destinationRangeStart = destinationRangeStart
        self.sourceRangeStart = sourceRangeStart
        self.rangeLength = rangeLength

class AlmanacMap:
    sourceType: str = ""
    destinationType: str = ""
    ranges: list[AlmanacMapRange] = list[AlmanacMapRange]()

    def lookup(self, sourceId: int) -> int:
        #print(f"sourceId: {sourceId}")
        # for r in self.ranges:
        #     pprint(vars(r))
        #     print(f"Conclusion (filter): {r.sourceRangeStart <= sourceId and (r.sourceRangeStart + r.rangeLength) > sourceId}")
        filteredRanges = [r for r in self.ranges if r.sourceRangeStart <= sourceId and (r.sourceRangeStart + r.rangeLength) > sourceId]
        #print(f"looking up {sourceId}: {len(filteredRanges)}")
        #pprint(filteredRanges)

        if len(filteredRanges) != 1:
            # If not mapped, then return as is
            if DEBUG:
                print(f"{self.sourceType} {sourceId} mapped {len(filteredRanges)} times")
            return sourceId

        range = filteredRanges[0]
        offset = sourceId - range.sourceRangeStart

        return range.destinationRangeStart + offset

    def __init__(self, sourceType: str, destinationType: str):
        self.sourceType = sourceType
        self.destinationType = destinationType

class Almanac:
    maps = dict[str, AlmanacMap]()

    _prevType: str = ""
    _nextType: str = ""
    _prevId: int = 0

    def lookup(self, sourceType: str, sourceId: int, destinationType: str | None = None) -> int:
        map = self.maps[sourceType]

        if destinationType == None:
           destinationType = self.getNextType(sourceType)
        
        self._prevType = sourceType
        self._nextType = map.destinationType
        self._prevId = sourceId
        
        while True:
            map = self.maps[self._prevType]
            self._prevId = map.lookup(self._prevId)
            if DEBUG:
                print(f"[mapping] {self._prevType} -> {self._nextType} = {self._prevId}")

            if self._nextType == destinationType:
                break

            self._prevType = self._nextType
            self._nextType = self.getNextType(self._nextType)

        return self._prevId

    def getNextType(self, sourceType: str) -> str:
        return self.maps[sourceType].destinationType

seeds = list[Seed]()
# seed_to_soil = AlmanacMap()
# soil_to_fertilizer = AlmanacMap()
# fertilizer_to_water = AlmanacMap()
# water_to_light = AlmanacMap()
# light_to_temperature = AlmanacMap()
# temperature_to_humidity = AlmanacMap()
# humidity_to_location = AlmanacMap()

almanac = Almanac()

total = 0

# -----------
# | Parsing |
# -----------

currentSourceType: str | None = None
for line in input_lines:
    line = line.replace("\n", "")

    if line.startswith("seeds: "):
        for seed_id in re.findall(r"(\d+)", line):
            seed = Seed()
            seed.id = int(seed_id)
            seeds.append(seed)
        #pprint(seeds)

    if line.endswith(" map:"):
        match = re.findall(r"(\w+)-to-(\w+) map:", line)
        sourceType = match[0][0]
        destinationType = match[0][1]
        print(f"{sourceType} -> {destinationType}")
        currentSourceType = sourceType
        map = AlmanacMap(sourceType, destinationType)
        almanac.maps[sourceType] = map
    elif currentSourceType is not None:
        match = line.split(" ")

        # Skip empty lines
        if len(match) < 3:
            continue

        destinationRangeStart = int(match[0])
        sourceRangeStart = int(match[1])
        rangeLength = int(match[2])

        mapRange = AlmanacMapRange(destinationRangeStart, sourceRangeStart, rangeLength)
        if not almanac.maps[currentSourceType].ranges:
            almanac.maps[currentSourceType].ranges = list[AlmanacMapRange]()
        almanac.maps[currentSourceType].ranges.append(mapRange)

print()
# --------------
# | Processing |
# --------------

global resultSet
resultSet: list[tuple[int, int]] = []
for seed in seeds:
    seedId = seed.id
    locationId = almanac.lookup("seed", seed.id, "location")
    resultSet.append((seedId, locationId))

resultSet.sort(key=lambda t : t[1])

for result in resultSet:
    print(f"Seed {result[0]} -> Location {result[1]}")

print(f"The smallest location number is {resultSet[0][1]} for seed {resultSet[0][0]}.")

print()
#print(f"Test 52: {almanac.lookup("fertilizer", 52, "water")}")
#pprint(almanac, depth=10)
#pprint(json.dumps(vars(almanac)))
# for map in almanac.maps:
#     pprint(vars(almanac.maps[map]))
#     pprint(len(almanac.maps[map].ranges))

#print("total: " + str(total))