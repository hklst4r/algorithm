cases = int(input())
import time
time.sleep(1)
for i in range(cases):
    n = int(input())
    arr = input().split()
    arr = [int(x) for x in arr]
    arr.sort()
    ans = 0
    for j in range(n//2):
        ans += arr[n-j-1] - arr[j]
    print(ans)

