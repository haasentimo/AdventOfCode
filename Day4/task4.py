res_counter = 0
counter_2 = 0

with open("input.txt") as file:
    for line in file.readlines():
        elf_1, elf_2 = line.split(",")
        start_e1, end_e1 = elf_1.split("-")
        start_e2, end_e2 = elf_2.split("-")

        if int(start_e1) >= int(start_e2) and int(end_e1) <= int(end_e2) or int(start_e1) <= int(start_e2) and int(end_e1) >= int(end_e2):
            res_counter += 1

        if int(start_e1) in range(int(start_e2), int(end_e2)+1) or int(end_e1) in range(int(start_e2), int(end_e2)+1):
            counter_2 += 1
        elif int(start_e2) in range(int(start_e1), int(end_e1)+1) or int(end_e2) in range(int(start_e1), int(end_e1)+1):
            counter_2 += 1

print(res_counter)
print(counter_2)
