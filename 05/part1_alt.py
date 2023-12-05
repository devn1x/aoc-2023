from pprint import pprint
import re

from numpy import source

input_file = open("input/example.txt")
#input_file = open("input/input.txt")
input_str = input_file.read()

seeds = list[int]()

# Path for each seed
path = dict[int, list[int]]()

total = 0

for block in input_str.split("\n\n"):
    lines = block.splitlines()

    #pprint(lines)

    if lines[0].startswith("seeds: "):
        for seed_id in re.findall(r"(\d+)", lines[0]):
            seeds.append(int(seed_id))
        continue

    title = lines.pop(0).replace(" map:", "")
    print(title)
    
    lines.sort(reverse=True)
    for line in lines:
        line_match = re.match(r"(\d+) (\d+) (\d+)", line)
        if line_match is None:
            print("fuck")
            exit()
        
        #pprint(line_match.groups())

        source_start = int(line_match.group(1))
        destination_start = int(line_match.group(2))
        length = int(line_match.group(3))

        for seed in seeds:
            if seed < source_start:
                continue

            if seed >= source_start + length:
                continue
                
            #print(f"{seed}: {line}")
            print(f"{seed}: {destination_start} + ({seed} - {source_start}) =")
            mapped_value = destination_start + (seed - source_start)
            print(f"  {mapped_value}")

            if seed not in path.keys():
                path[seed] = list[int]()

            path[seed].append(mapped_value)
        #print(line)
        

print()
print("total: " + str(total))