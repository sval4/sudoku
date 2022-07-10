bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]


horizontal_counter = 3
vertical_counter = 3
check1 = False
check2 = False
for i in range(len(bd)):
    if horizontal_counter == 3:
        horizontal_counter = 0
        if i == 0:
            print("-" * (2 * (len(bd[0]) + (len(bd[0]) // 3)) + 1), end = "")
        else:
            print()
            print("-" * (2 * (len(bd[0]) + (len(bd[0]) // 3)) + 1), end = "")
        check1 = True
    print()
    for j in range(len(bd[i])):
        if vertical_counter == 3:
            check2 = True
            vertical_counter = 0
            if j == 0:
                print("|", end = "")
            else:
                print(" |", end = "")
        print(" " + bd[i][j], end = "")
        if j == len(bd[i]) - 1:
            print(" |", end = "")
        if check2:
            check2 = False
            j -= 1
        vertical_counter += 1
    if check1:
        check1 = False
        i -= 1
    horizontal_counter += 1
print()
print("-" * (2 * (len(bd[0]) + (len(bd[0]) // 3)) + 1), end = "")

