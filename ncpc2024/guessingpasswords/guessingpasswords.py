n, m = map(int, input().split())

first = list(input())

y_c = first.count("Y")

a = y_c + 1

lst = []

used = [set() for _ in range(m)]
out = []
inp_l = []
inp_l.append(first)
for _ in range(n-1):
    inp_l.append(list(input()))
for inp in inp_l:
    i = 0
    st = []
    c = 0
    for el in inp:
        if not el == "Y":
            st.append(a)
            a += 1
        else:
            hit = False
            for j in range(c, y_c):
                if not j in used[i]:
                    print(j)
                    c += 1
                    st.append(j)
                    hit = True
                    used[i].add(j)
                    break
            if not hit:
                print(inp)
                print(used)
                print("Bugged!")
                exit()
        i += 1
    out.append(" ".join([str(x) for x in st])) 
b = int(input())

output = [-1] * m
for i in range(y_c):
    for j in range(len(used)):
        if i not in used[j]:
            output[j] = i

for i in range(len(output)):
    if output[i] != -1:
        continue
    output[i] = a
    a += 1



if a > b:
    print("Bugged!")
    exit()
else:
    for el in out:
        print(el)
    print(" ".join([str(x) for x in output]))






