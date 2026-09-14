inp = int(input())
out = []
if inp % 2 == 1:
    inp -= 3 
    out.append("3")

while inp > 0:
    out.append("2")
    inp -= 2
print(len(out))
print(" ".join(out))
    
    
