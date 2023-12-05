from pprint import pprint
import re

input_file = open("input/example.txt")
#input_file = open("input/input.txt")
input_lines = input_file.readlines()

class Seed:
    id: int

    def __repr__(self) -> str:
        return str(vars(self))

class AlmanacMap:
    

    def lookup(self, source_id: int):
        pass
    pass

class AlmanacMapRange:
    pass

seeds = list[Seed]()
seed_to_soil = AlmanacMap()
soil_to_fertilizer = AlmanacMap()
fertilizer_to_water = AlmanacMap()
water_to_light = AlmanacMap()
light_to_temperature = AlmanacMap()
temperature_to_humidity = AlmanacMap()
humidity_to_location = AlmanacMap()

total = 0

for line in input_lines:
    line = line.replace("\n", "")

    #print(line)

    if line.startswith("seeds: "):
        for seed_id in re.findall(r"(\d+)", line):
            seed = Seed()
            seed.id = seed_id
            seeds.append(seed)
        
        pprint(seeds)

    if 

print()
print("total: " + str(total))