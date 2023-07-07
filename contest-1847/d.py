import sys
import time
n, m, q = sys.stdin.readline()[:-1].split(" ")
beginTime = time.time()
n = int(n)
m = int(m)
q = int(q)
# time.sleep(1)
# print()
s = list(sys.stdin.readline()[:-1])
s = [int(x) for x in s]
slices = []
ranges = set()
for i in range(m):
    ii, jj = sys.stdin.readline()[:-1].split(" ")
    ii = int(ii) - 1
    jj = int(jj) - 1
    for j in range(ii, jj + 1):
        if j not in ranges:
            slices.append(j)
    ranges.update(range(ii, jj+ 1))

lenOfSlices = len(slices)
onesNum = s.count(1)

for i in range(q):
    conflict = {}
    for i in range(n):
        conflict[i] = False

    idx = int(sys.stdin.readline()[:-1]) - 1
    if s[idx] == 0:
        onesNum += 1
    else:
        onesNum -= 1
    s[idx] ^= 1
    cnt = 0
    operations = 0
    flag = False
    # print("s", s)
    # print("onesNum", onesNum)
    mCurr = min(onesNum, lenOfSlices)
    for j in range(mCurr):
        if s[slices[j]] == 0:
            operations += 1
    
    print(operations)

endTime = time.time()

print(f"total time: {endTime - beginTime}")