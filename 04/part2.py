import math
import re

#input_file = open("input/example.txt")
input_file = open("input/input.txt")
input_lines = input_file.readlines()

class ScratchCard:
    id: int
    winning_numbers: list[int]
    played_numbers: list[int]

    def points(self) -> int:
        correct_guesses = 0

        for wn in self.winning_numbers:
            if wn in self.played_numbers:
                correct_guesses += 1

        print(f"{correct_guesses} -> {math.floor(2 ** (correct_guesses - 1))}")
        return math.floor(2 ** (correct_guesses - 1))

scratch_cards = list[ScratchCard]()

total = 0

for line in input_lines:
    line = line.replace("\n", "")

    #print(line)

    numbers = re.findall(r"(\d+)", line)
    numbers = list(map(int, numbers))

    card = ScratchCard()
    card.id = numbers[0]
    card.winning_numbers = numbers[1:11]
    card.played_numbers = numbers[11:]

    scratch_cards.append(card)

    points = card.points()
    total += points
    print(f"Card {card.id}: {points} points")
    #print(f"Card {card.id}: {points} points")

    #total += int(calibration)
    #print(calibration)

print()
print("total: " + str(total))