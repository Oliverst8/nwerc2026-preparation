n = int(input())

def quit(i):
        print("error", i+1)    
        exit()

prev: tuple[int, int] = 0,0
prevRound = 0
for i in range(n):
    a, b = map(int, input().split("-"))
    # print(a, b)
    round = a+b;
    alice = ((round+1)//2) % 2 == 0
    if not alice:
        b, a = a, b
    diff = (a - prev[0]), (b - prev[1]) 
    # print("prev: ", prev)
    # print("diff: ", diff)
    # print("a, b: ", a, b)
    if diff[0] < 0 or  diff[1] < 0:
        quit(i)
    if (prev[0] >= 11 or prev[1] >= 11) and (diff[0] != 0 or diff[1] != 0):
        quit(i)
    if a == 11 and b == 11:
        quit(i)


    prev = a, b
    prevRound = round

print("ok")

            



