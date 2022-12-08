lost = 0
draw = 3
win = 6

rock = 1
paper = 2
scissor = 3

with open("input.txt") as file:
    total_score = 0
    for line in file.readlines():
        opponent, you = line.replace("\n", "").split(" ")
        if opponent == "A" and you == "X":
            total_score += draw + rock
        elif opponent == "A" and you == "Y":
            total_score += win + paper
        elif opponent == "A" and you == "Z":
            total_score += lost + scissor
        elif opponent == "B" and you == "X":
            total_score += lost + rock
        elif opponent == "B" and you == "Y":
            total_score += draw + paper
        elif opponent == "B" and you == "Z":
            total_score += win + scissor
        elif opponent == "C" and you == "X":
            total_score += win + rock
        elif opponent == "C" and you == "Y":
            total_score += lost + paper
        elif opponent == "C" and you == "Z":
            total_score += draw + scissor
        else:
            print("this is bad")

print(total_score)