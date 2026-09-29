n = int(input())

arr = list(map(int, input().split()))

peaking = arr[1] > arr[0]
peaks = []
mx = 0 
mn = arr[0]
if peaking:
    peaks.append(arr[0])

for i in range(1, n):
    if peaking == (arr[i] < arr[i-1]) and (not (arr[i] == arr[i-1])):
        peaking = not peaking
        peaks.append(arr[i-1])

if not peaking:
    peaks.append(arr[-1])

for i in range(1, len(peaks)-1, 2):
    mx = max(min(peaks[i] - peaks[i-1], peaks[i] - peaks[i+1]), mx)

print(mx)





            
    






