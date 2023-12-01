import re

input_file = open("input/input.txt")
input_lines = input_file.readlines()

total = 0

for line in input_lines:
    line = line.replace("\n", "")

    #print(line)

    digits = re.findall(r"\d", line)

    calibration = digits[0] + "" + digits[-1]
    total += int(calibration)
    print(calibration)

print()
print("total: " + str(total))