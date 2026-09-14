n , k = map(int, input().split())

final = 0

a = 1
for _ in range(k):
    a = a*k + 1
new_a = 1
new_n = min(n, a)
for _ in range(k):
    new_a = new_a*k + 1
    final += new_n // new_a
    # print("res, div, a ", final, new_n // new_a, new_a)

if n - a > 0:
    print(final + n - a)
else:
    print(final)

