import re

def words_to_digits(input: str):
    return input.replace("one", "1") \
        .replace("two", "2") \
        .replace("three", "3") \
        .replace("four", "4") \
        .replace("five", "5") \
        .replace("six", "6") \
        .replace("seven", "7") \
        .replace("eight", "8") \
        .replace("nine", "9")

input_file = open("input/input.txt")
input_lines = input_file.readlines()

total = 0

for line in input_lines:
    line = line.replace("\n", "")

    #print(line)

    digits = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)

    print(digits)

    first_digit = words_to_digits(str(digits[0]))
    last_digit = words_to_digits(str(digits[-1]))

    calibration = first_digit + "" + last_digit
    total += int(calibration)
    print(calibration)

print()
print("total: " + str(total))