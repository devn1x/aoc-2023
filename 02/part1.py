import re
from typing import Any, Tuple

input_file = open("input/input.txt")
input_lines = input_file.readlines()

limit_red = 12
limit_green = 13
limit_blue = 14

total = 0

def match_line(line: str) -> Tuple[int, str]:
    match = re.match(r"Game (?P<gid>\d+): (.+)", line)

    if match is None:
        print("fuck")
        exit()

    game_id = int(match.group(1))
    reveals = match.group(2)
    return (game_id, reveals)

def match_reveals(reveals_str: str) -> list[Tuple[int,int,int]]:
    return_value = list[Tuple[int,int,int]]()

    reveals = re.findall(r"([^;\n]+)", reveals_str)
    for reveal in reveals:
        reveal = str(reveal)
        reveal_match = re.match(r"(?:(?:(?P<red>\d+) red|(?P<green>\d+) green|(?P<blue>\d+) blue)(?:, )?)+", reveal.strip())

        if reveal_match is None:
            print("fuck: " + reveal)
            exit()
        
        red = int(reveal_match.group("red") or 0)
        green = int(reveal_match.group("green") or 0)
        blue = int(reveal_match.group("blue") or 0)

        return_value.append((red, green, blue))
    return return_value

def is_valid(game: list[Tuple[int,int,int]]) -> bool:
    return_value = True

    for reveal in game:
        r, g, b = reveal

        if r > limit_red or g > limit_green or b > limit_blue:
            return_value = False
            break

    return return_value

for line in input_lines:
    line = line.replace("\n", "")

    game_id, reveals = match_line(line)
    game = match_reveals(reveals)
    game_is_valid = is_valid(game)

    if game_is_valid:
        total += game_id

    print("Game " + str(game_id) + ": " + str(game_is_valid))

print()
print("total: " + str(total))