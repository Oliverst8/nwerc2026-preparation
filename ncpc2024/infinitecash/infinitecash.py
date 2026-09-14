import math
def parse(stri):
    S = 0
    for c in stri:
        S = S << 1
        if c == "1":
            S += 1
    return S


s = parse(input())
d = parse(input())
m = parse(input())

day = 0
while (m > 0):
    print(math.log2(m))
    m = m >> 1
    if day % d == 0:
        m += s
    if day > d*10:
        print("Infinite money!")
        exit()
    day += 1
print(str(bin(day-1))[2:])



