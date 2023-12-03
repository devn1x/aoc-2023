import re
from typing import Tuple

class PartNumber:
    index: int
    length: int
    value: int

def find_gears(line: str) -> list[int]:
    return_value = list[int]()

    for match in re.finditer(r"[*]", line):
        return_value.append(match.start())
    
    return return_value

def find_numbers(line: str) -> list[PartNumber]:
    return_value = list[PartNumber]()

    for match in re.finditer(r"(\d+)", line):
        part_no = PartNumber()
        part_no.index = match.start()
        part_no.length = match.end() - match.start()
        part_no.value = int(match.group(0))
        #pprint(vars(part_no))

        return_value.append(part_no)
    
    return return_value

def find_corresponding_gears(line_no: int, number: PartNumber, symbols: dict[int, list[int]]) -> list[Tuple[int,int]]:
    return_value = list[Tuple[int,int]]()

    # Before
    if (number.index - 1) in symbols[line_no]:
        #print(f"{number.value}: before")
        return_value.append((line_no, number.index - 1))
    # After
    if (number.index + number.length) in symbols[line_no]:
        #print(f"{number.value}: after")
        return_value.append((line_no, number.index + number.length))

    # Above and below for each digit
    for digit_index in range(number.index, number.index + number.length):
        # Above
        if line_no > 0:
            #print(f"{line_no} above")
            if digit_index - 1 in symbols[line_no - 1]:
                #print(f"{number.value}: above left")
                return_value.append((line_no - 1, digit_index - 1))
                break
            if digit_index in symbols[line_no - 1]:
                #print(f"{number.value}: above")
                return_value.append((line_no - 1, digit_index))
                break
            if digit_index + 1 in symbols[line_no - 1]:
                #print(f"{number.value}: above right")
                return_value.append((line_no - 1, digit_index + 1))
                break

        # Below
        if line_no < len(symbols) - 1:
            #print(f"{line_no} below")
            if digit_index - 1 in symbols[line_no + 1]:
                #print(f"{number.value}: below left")
                return_value.append((line_no + 1, digit_index - 1))
                break
            if digit_index in symbols[line_no + 1]:
                #print(f"{number.value}: below")
                return_value.append((line_no + 1, digit_index))
                break
            if digit_index + 1 in symbols[line_no + 1]:
                #print(f"{number.value}: below right")
                return_value.append((line_no + 1, digit_index + 1))
                break

    return return_value


#input_file = open("input/example.txt")
input_file = open("input/input.txt")
input_lines = input_file.readlines()

total = 0

line_no = 0
gears = dict[int,list[int]]()
numbers = dict[int,list[PartNumber]]()

parts_per_gear = dict[Tuple[int,int], list[PartNumber]]()

for line in input_lines:
    line = line.replace("\n", "")

    #print(line)

    gears[line_no] = find_gears(line)
    numbers[line_no] = find_numbers(line)

    line_no += 1

for key, value in numbers.items():
    #print(f"{key} {value}")
    for number in value:
        corresponding_gears = find_corresponding_gears(key, number, gears)

        #if is_valid:
        #    total += number.value
        for gear_coords in corresponding_gears:
            if gear_coords not in parts_per_gear.keys():
                parts_per_gear[gear_coords] = list[PartNumber]()

            parts_per_gear[gear_coords].append(number)

#pprint(parts_per_gear)

for gear_coords, part_numbers in parts_per_gear.items():
    #print(len(part_numbers))
    if len(part_numbers) == 2:
        total += part_numbers[0].value * part_numbers[1].value


print()
print(f"total: {total}")