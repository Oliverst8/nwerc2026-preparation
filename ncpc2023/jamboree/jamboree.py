from heapq import _heapify_max, heapify
import heapq


N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort(key = lambda x: -x)

output = []
for i in range(M):
    if i >= len(lst): 
        break
    output.append(lst[i])

j = len(output) -1
for i in range(M, len(lst)):
    output[j] += lst[i]
    j -= 1

print(max(output))

