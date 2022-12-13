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
    tmp = pop_from_stack(amount, root)
    append_to_stack(destination, tmp)

def pop_from_stack(number, stack):
    n = int(stack)
    number = int(number)
    cargo = None
    if n == 1:
         cargo = stack_1[-number:]
         del stack_1[-number:]
    elif n== 2:
        cargo = stack_2[-number:]
        del stack_2[-number:]
    elif n == 3:
        cargo = stack_3[-number:]
        del stack_3[-number:]
    elif n == 4:
        cargo = stack_4[-number:]
        del stack_4[-number:]
    elif n == 5:
        cargo = stack_5[-number:]
        del stack_5[-number:]
    elif n == 6:
        cargo = stack_6[-number:]
        del stack_6[-number:]
    elif n == 7:
        cargo = stack_7[-number:]
        del stack_7[-number:]
    elif n == 8:
        cargo = stack_8[-number:]
        del stack_8[-number:]
    elif n == 9:
        cargo = stack_9[-number:]
        del stack_9[-number:]
    return cargo

def append_to_stack(number, cargo):
    n = int(number)
    if n == 1:
        for item in cargo:
            stack_1.append(item)
    elif n== 2:
        for item in cargo:
            stack_2.append(item)
    elif n == 3:
        for item in cargo:
            stack_3.append(item)
    elif n == 4:
        for item in cargo:
            stack_4.append(item)
    elif n == 5:
        for item in cargo:
            stack_5.append(item)
    elif n == 6:
        for item in cargo:
            stack_6.append(item)
    elif n == 7:
        for item in cargo:
            stack_7.append(item)
    elif n == 8:
        for item in cargo:
            stack_8.append(item)
    elif n == 9:
        for item in cargo:
            stack_9.append(item)

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
    result += pop_from_stack(1, i)[0]



print(result)

