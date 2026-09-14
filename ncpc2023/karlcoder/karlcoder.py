def buf(i: int):
    return (f"buf[{i}]\n")
def strlen(res: int):
    print(f"strlen(buf) = {res}")
n = 2

while True:
    res = int(input(buf(n*2-1)))
    if res != 0:
        n *= 2
    else:
        break

start = n
end = n*2
while start <= end:
    mid = (start + end) // 2
    res = int(input(buf(mid)))
    if res == 0:
        end = mid - 1
    else:
        start = mid 
strlen(start)








