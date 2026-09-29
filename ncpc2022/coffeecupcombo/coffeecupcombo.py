lectures = int(input())

c = 0

inp = input()

amount = 0
for el in inp:
    if el == "1":
        c = 2
        amount += 1
    else:
        if c > 0:
            amount += 1
            c -= 1
print(amount)


