from typing import NamedTuple
import os


ROOT = "$ cd /"
LIST = "$ ls"
OUT = "$ cd .."

file = open("input.txt")

class File(NamedTuple):
    name: str
    size: int

directory_dict = {"root": []}

current_directory = ""

for line in file.readlines():
    line = line.replace("\n", "")
    if line == ROOT:
        current_directory = "root"
    elif line == LIST:
        continue
    elif line[:5] == "$ cd ":
        current_directory = os.path.normpath(os.path.join(current_directory, line[5:]))
        if current_directory not in directory_dict:
            directory_dict[current_directory] = []
    else:
        data = ""
        if line[:4] == "dir ":
            data = os.path.normpath(os.path.join(current_directory, line[4:]))
        else:
            size, name = line.split(" ")
            data = File(name, int(size))

        directory_dict[current_directory].append(data)


directory_size = {}

def calculate_sum_of_dir(name:str):
    sum = 0

    for item in directory_dict[name]:
        if isinstance(item, str):
            sum += calculate_sum_of_dir(item)
        else:
            sum += item.size
    directory_size[name] = sum
    return sum



result = 0
for key in directory_dict.keys():
    size = calculate_sum_of_dir(key)
    if size <= 100000:
        result += size
print(result)

total_space = 70000000
used_space = calculate_sum_of_dir("root")
needed_space = 30000000
min_del_space = needed_space - (total_space - used_space)

print(min_del_space)

possible_deletions = []

for key in directory_dict.keys():
    size = calculate_sum_of_dir(key)
    if size >=min_del_space:
        possible_deletions.append(size)

print(min(possible_deletions))
