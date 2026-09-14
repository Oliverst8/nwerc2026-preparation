import sys


sys.setrecursionlimit(10**5)

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
def convert(str: str):
    if len(str) == 1:
        return m[str]
    if len(str) == 0:
        return 0
    a = -1
    l = "j"
    for i in range(len(str)):
        c = str[i]
        if m[c] > m[l]:
            a = i
            l = c
    pre = convert(str[:a])
    post = convert(str[a+1:])
    return m[l]-pre+post
for _ in range(n):
    print(convert(input()))

