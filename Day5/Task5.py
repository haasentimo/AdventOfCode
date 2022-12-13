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
        tmp = root.pop()
        destination.append(tmp)

def get_correct_stack(number):
    n = int(number)
    if n == 1:
        return stack_1
    elif n== 2:
        return stack_2
    elif n == 3:
        return stack_3
    elif n == 4:
        return stack_4
    elif n == 5:
        return stack_5
    elif n == 6:
        return stack_6
    elif n == 7:
        return stack_7
    elif n == 8:
        return stack_8
    elif n == 9:
        return stack_9

got_empty_line = False
for line in file.readlines():
    if line == "\n":
        got_empty_line = True
    elif not got_empty_line:
        continue
    else:
        line =line.replace("move ", "")
        amount_to_move = line[:2]
        line = line.replace(" from ", "")
        line = line.replace("from ", "")
        root_stack = line[:1]
        line = line.replace(" to ", "")
        destination_stack = line[:1]
        move_cargo(amount_to_move, get_correct_stack(root_stack), get_correct_stack(destination_stack))

result = ""
for i in range(1, 10):
    tmp = get_correct_stack(i)
    result += tmp.pop()

print(result)

