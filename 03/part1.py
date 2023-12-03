from pprint import pprint
import re
from typing import Tuple

class PartNumber:
    index: int
    length: int
    value: int

def find_symbols(line: str) -> list[int]:
    return_value = list[int]()

    for match in re.finditer(r"[^\d.]", line):
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

def is_valid_number(line_no: int, number: PartNumber, symbols: dict[int, list[int]]) -> bool:
    # Before
    if (number.index - 1) in symbols[line_no]:
        print(f"{number.value}: before")
        return True
    # After
    if (number.index + number.length) in symbols[line_no]:
        print(f"{number.value}: after")
        return True

    # Above and below for each digit
    for digit_index in range(number.index, number.index + number.length):
        # Above
        if line_no > 0:
            #print(f"{line_no} above")
            if digit_index - 1 in symbols[line_no - 1]:
                print(f"{number.value}: above left")
                return True
            if digit_index in symbols[line_no - 1]:
                print(f"{number.value}: above")
                return True
            if digit_index + 1 in symbols[line_no - 1]:
                print(f"{number.value}: above right")
                return True
            pass

        # Below
        if line_no < len(symbols) - 1:
            #print(f"{line_no} below")
            if digit_index - 1 in symbols[line_no + 1]:
                print(f"{number.value}: below left")
                return True
            if digit_index in symbols[line_no + 1]:
                print(f"{number.value}: below")
                return True
            if digit_index + 1 in symbols[line_no + 1]:
                print(f"{number.value}: below right")
                return True
            pass

    return False


#input_file = open("input/example.txt")
input_file = open("input/input.txt")
input_lines = input_file.readlines()

total = 0

line_no = 0
symbols = dict[int,list[int]]()
numbers = dict[int,list[PartNumber]]()

for line in input_lines:
    line = line.replace("\n", "")

    #print(line)

    symbols[line_no] = find_symbols(line)
    numbers[line_no] = find_numbers(line)

    line_no += 1

for key, value in numbers.items():
    #print(f"{key} {value}")
    for number in value:
        is_valid = is_valid_number(key, number, symbols)

        if is_valid:
            total += number.value

print()
print("total: " + str(total))