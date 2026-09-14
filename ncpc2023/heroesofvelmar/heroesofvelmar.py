chars = {
        "Shadow": 6,
        "Gale": 5,
        "Ranger": 4,
        "Anvil": 7,
        "Vexia": 3,
        "Guardian": 8,
        "Thunderheart": 6,
        "Frostwhisper": 2,
        "Voidclaw": 3,
        "Ironwood": 3,
        "Zenith": 4,
        "Seraphina": 1
        }
loc = [0,0,0]


for i in range(6):
    mult = 1 if i%2 == 0 else -1
    inp = input().split()
    count = int(inp[0])
    for char in inp[1:]:
        loc[i//2] += mult * chars[char]
        if char == "Thunderheart" and count == 4:
            loc[i//2] += 6 * mult
        elif char == "Zenith" and i // 2 == 1:
            loc[i//2] += 5 * mult
        elif char == "Seraphina":
            loc[i//2] += mult * (count-1)

def checkWon():
    cntA = 0
    cntB = 0
    cntC = 0
    for el in loc:
        if el > 0:
            cntA += 1
        elif el < 0:
            cntB += 1
        else:
            cntC += 1
    if cntA == cntB:
        res = sum(loc)
        if res > 0:
            print("Player 1")
            exit()
        if res < 0:
            print("Player 2")
            exit()
        else:
            print("Tie")
    elif cntA > cntB:
        print("Player 1")
    else:
        print("Player 2")

checkWon()





        



