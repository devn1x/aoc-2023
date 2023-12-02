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

def min_cubes(game: list[Tuple[int,int,int]]) -> Tuple[int,int,int]:
    max_r = 0
    max_g = 0
    max_b = 0

    for reveal in game:
        r, g, b = reveal

        if r > max_r:
            max_r = r
        
        if g > max_g:
            max_g = g

        if b > max_b:
            max_b = b

    return (max_r, max_g, max_b)

for line in input_lines:
    line = line.replace("\n", "")

    game_id, reveals = match_line(line)
    game = match_reveals(reveals)
    min_cubes_r, min_cubes_g, min_cubes_b = min_cubes(game)

    game_total = min_cubes_r * min_cubes_g * min_cubes_b
    total += game_total

    print("Game " + str(game_id) + ": " + str(game_total))

print()
print("total: " + str(total))