def compare(die1, die2):
    cnt = 0
    possible = 36 
    for el in die1:
        for el2 in die2:
            if el > el2:
                cnt += 1
            elif el == el2:
                possible -= 1
    if possible == 0:
        return 0
    return cnt/possible

dice: list[list[int]] = []
for _ in range(3):
    dice.append(list(map(int, input().split())))

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        d1 = compare(dice[i], dice[(i+2)%3])
        d2 = compare(dice[i], dice[(i+1)%3])
        if d1 >= 0.5 and d2 >= 0.5:
            print(i+1)
            exit()
print("No dice")
