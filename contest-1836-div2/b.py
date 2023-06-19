
import time
time.sleep(3)

cases = int(input())

for _ in range(cases):
    n, k, g = input().split(" ")
    n = int(n)
    k = int(k)
    g = int(g)

    if g % 2 == 0:
        rest = k * g - (n-1) * (g//2 - 1)
    else:
        rest = k * g - (n-1) * (g//2)
    
    if rest < g/2:
        print(k * g)
    else:
        r = rest % g
        if r >= g/2:
            print(k * g - ((rest//g + 1) * g))
        else:
            print(k * g - ((rest//g) * g))