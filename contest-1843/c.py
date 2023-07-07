cases = int(input())

import time
time.sleep(1)

for _ in range(cases):
    n = int(input())

    ans = 0

    while n != 0:
        ans += n
        n = n // 2
    
    print(ans)