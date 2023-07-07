import sys
import time
cases = int(sys.stdin.readline()[:-1])

for i in range(cases):
    n, k = sys.stdin.readline()[:-1].split(" ")
    n = int(n)
    k = int(k)

    a = sys.stdin.readline()[:-1].split(" ")
    a = [int(x) for x in a]
    s = []
    for i in range(len(a) - 1):
        s.append(abs(a[i] - a[i+1]))
    
    s.sort(reverse=True)
    ans = sum(s[k-1:])

    print(ans)


