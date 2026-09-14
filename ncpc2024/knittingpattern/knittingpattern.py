n, p = map(int, input().split())
res = (n-p)%(2*p)
if res == p:
    print(0)
else:
    print(res)
