
m = {
        "j": -1,
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

n = int(input())
for _ in range(n):
    str = input()
    num = str[::-1]
    top, out = 0,0
    for char in num:
        val = m[char]
        top = max(top, val)
        mult = -1 if val < top else 1
        out += mult * val
    print(out)



