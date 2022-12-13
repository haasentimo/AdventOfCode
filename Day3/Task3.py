import string

prio_dict = {}

for letter, value in zip(string.ascii_lowercase, range(1,27)):
    prio_dict[letter] = value

for letter, value in zip(string.ascii_uppercase, range(27, 53)):
    prio_dict[letter] = value

result_1 = 0
result_2 = 0

file = open("input.txt")
for line in file.readlines():
    middle_index = int(len(line)/2)
    compartment_1 = line[:middle_index]
    compartment_2 = line[middle_index:]

    for char in compartment_1:
        if char in compartment_2:
            result_1 += prio_dict[char]
            break

file = open("input.txt")
lines = [line for line in file.readlines()]
tmp = []

for line in lines:
    tmp.append(line)
    if len(tmp) == 3:
        for char in tmp[0]:
            if char in tmp[1] and char in tmp[2]:
                result_2 += prio_dict[char]
                break
        tmp = []
print(result_1)
print(result_2)