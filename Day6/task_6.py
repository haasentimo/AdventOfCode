
with open("input.txt") as file:
    data = file.read()

    counter = 0
    marker = []

    for char in data:
        counter += 1
        if not char in marker:
            marker.append(char)
            if len(marker) == 14:
                print("hit")
                break
        else:
            tmp = []
            found = False
            for element in marker:
                if not element == char:
                    if found:
                        tmp.append(element)
                    else:
                        continue
                else:
                    found = True
            tmp.append(char)
            marker = tmp

print(counter)