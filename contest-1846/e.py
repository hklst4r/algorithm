cases = int(input())

import sys
import time
import math

possible = []

for i in range(2, 10 ** 6):
    curr =  1 + i
    tmp = i*i
    while True:
        curr += tmp
        if curr > 10 ** 18:
            break
        else:
            possible.append(curr)
            tmp *= i

possible.sort()

def isIn(n, arr):
    size = len(arr)
    if size == 0:
        return 0
    left = 0
    right = size - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < n:
            left = mid + 1
        else:
            right = mid
    if arr[left] == n:
        return True
    else:
        return False

for _ in range(cases):
    n = int(sys.stdin.readline()[:-1])
    if n < 7:
        print("NO")
        continue
    if isIn(n, possible):
        print("YES")
        continue
    
    nM1 = n - 1
    k = int(math.sqrt(nM1))
    if k * (k + 1) == nM1:
        print("YES")
        continue

    print("NO")