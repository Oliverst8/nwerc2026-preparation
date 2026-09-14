xs, ys = map(int, input().split())
xt, yt = map(int, input().split())
xp, yp = map(int, input().split())

out: list[tuple[int,int]] = []
end = (-1, -1)
x_switch = True
if xs > xp:
    out.append((10**9, ys))
elif xs < xp:
    out.append((-10**9, ys))
else:
    if ys > yp:
        out.append((xs, 10**9))
        x_switch = False
    elif ys < yp:
        out.append((xs, -10**9))
        x_switch = False

if xt > xp:
    end = ((10**9, yt))
elif xt < xp:
    end = ((-10**9, yt))
else:
    if yt > yp:
        end = ((xt, 10**9))
    elif yt < yp:
        end = ((xt, -10**9))
cur = out[0]
if x_switch:
    cur = (cur[0], 10**9)
else:
    cur = (10**9, cur[1])
out.append(cur)
while not((((cur[0]) == (end[0]) == 10**9)) or (((cur[1]) == (end[1]) == 10**9)) or ((((cur[0]) == (end[0]) == -10**9)) or (((cur[1]) == (end[1]) == -10**9)))):
    if x_switch:
        cur = (cur[0], -1*cur[1])
    else:
        cur = (cur[0]*(-1), cur[1])
    x_switch = not x_switch
    out.append(cur)

out.append(end)

print(len(out))
for x, y in out:
    print(x, y)



