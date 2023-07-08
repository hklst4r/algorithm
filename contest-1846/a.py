cases = int(input())

import sys

for _ in range(cases):
    n = int(sys.stdin.readline()[:-1])
    ans = 0
    for i in range(n):
        a, b = sys.stdin.readline()[:-1].split(" ")
        a = int(a)
        b = int(b)

        if b < a:
            ans += 1

    print(ans)