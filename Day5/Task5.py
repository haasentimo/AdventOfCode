file = open("input.txt")

stack_1 = ["D", "H", "N", "Q", "T", "W", "V", "B"]
stack_2 = ["D", "W", "B"]
stack_3 = ["T", "S", "Q","W", "J", "C"]
stack_4 = ["F", "J", "R","N", "Z", "T", "P"]
stack_5 = ["G", "P", "V","J", "M", "S", "T"]
stack_6 = ["B", "W", "F","T", "N"]
stack_7 = ["B", "L", "D","Q", "F", "H", "V", "N"]
stack_8 = ["H", "P", "F","R"]
stack_9 = ["Z", "S", "M","B", "L", "N", "P", "H"]

def move_cargo(amount, root, destination):
    for _ in range(0,int(amount)):
        tmp = pop_from_stack(root)
        append_to_stack(destination, tmp)

def pop_from_stack(number):
    n = int(number)
    if n == 1:
        return stack_1.pop()
    elif n== 2:
        return stack_2.pop()
    elif n == 3:
        return stack_3.pop()
    elif n == 4:
        return stack_4.pop()
    elif n == 5:
        return stack_5.pop()
    elif n == 6:
        return stack_6.pop()
    elif n == 7:
        return stack_7.pop()
    elif n == 8:
        return stack_8.pop()
    elif n == 9:
        return stack_9.pop()

def append_to_stack(number, cargo):
    n = int(number)
    if n == 1:
        stack_1.append(cargo)
    elif n== 2:
        stack_2.append(cargo)
    elif n == 3:
        stack_3.append(cargo)
    elif n == 4:
        stack_4.append(cargo)
    elif n == 5:
        stack_5.append(cargo)
    elif n == 6:
        stack_6.append(cargo)
    elif n == 7:
        stack_7.append(cargo)
    elif n == 8:
        stack_8.append(cargo)
    elif n == 9:
        stack_9.append(cargo)

got_empty_line = False
for line in file.readlines():
    if line == "\n":
        got_empty_line = True
    elif not got_empty_line:
        continue
    else:
        line =line.replace("move ", "")
        amount_to_move, line = (line[:2],line[2:])
        line = line.replace(" from ", "")
        line = line.replace("from ", "")
        root_stack, line = (line[:1],line[1:])
        line = line.replace(" to ", "")
        destination_stack, line = (line[:1],line[1:])
        move_cargo(amount_to_move, root_stack, destination_stack)

result = ""
for i in range(1, 10):
    result += pop_from_stack(i)

print(result)

