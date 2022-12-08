with open("input.txt") as file:
    list_of_elves = []
    elf_calories = 0
    for line in file.readlines():
        if not line == "\n":
            elf_calories += int(line)
        else:
            list_of_elves.append(elf_calories)
            elf_calories = 0

total_of_top_three = 0
for _ in range(0, 3):
    current_max = max(list_of_elves)
    total_of_top_three += current_max
    list_of_elves.remove(current_max)

print(total_of_top_three)
