with open("input.txt") as file:
    max_calories = 0
    elf_calories = 0
    for line in file.readlines():
        if not line == "\n":
            elf_calories += int(line)
        else:
            max_calories = max_calories if max_calories > elf_calories else elf_calories
            elf_calories = 0

print(max_calories)
