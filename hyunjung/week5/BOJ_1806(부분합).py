n, s = map(int, input().split(' '))
seq = list(map(int, input().split(' ')))
seqSum = []
sum = 0
for i in range(n):
    sum += seq[i]
    seqSum.append(sum)
st, ed = 0, 0
partSum = 0
minLength = float('inf')
while ed < n and st <= ed:
    if st == 0:
        partSum = seqSum[ed]
    else:
        partSum = seqSum[ed] - seqSum[st] + seq[st]
    if partSum >= s:
        minLength = min(ed-st+1, minLength)
        st += 1
    else:
        ed += 1
if minLength == float('inf'):
    print(0)
else:
    print(minLength)
