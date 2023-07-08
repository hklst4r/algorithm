cases = int(input())

import sys
import time
time.sleep(0.5)
def calculate(d, h, tmp):
    # print(tmp)
    if len(tmp) == 1:
        return d * h / 2
    ans = d * (h/2 + tmp[-1] - tmp[0])
    lessMainJi = 0
    for i in range(1, len(tmp)):
        yDiff = tmp[i] - tmp[i-1]
        xDiff = yDiff * d
        mianJi = xDiff * yDiff
        lessMainJi += mianJi
    ans -= lessMainJi / (2 * h)
    return ans
for _ in range(cases):
    n, d, h = sys.stdin.readline()[:-1].split(" ")
    n = int(n)
    d = int(d)
    h = int(h)

    y = sys.stdin.readline()[:-1].split(" ")
    y = [int(x) for x in y]

    yLast = -1 * 2 * d
    ans = 0
    tmp = []
    for i in range(n):
        # print(f"i: {i}, {y[i]}")
        yCurr = y[i]
        if i == 0:
            tmp.append(yCurr)
        elif yCurr - yLast >= h:
            ans += calculate(d, h, tmp)
            tmp = [yCurr]
        else:
            tmp.append(yCurr)
        if i == n - 1:
            ans += calculate(d, h, tmp)
            break
        yLast = yCurr
    
    print(ans)