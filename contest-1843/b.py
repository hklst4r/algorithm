cases = int(input())

import time 
time.sleep(1)
for i in range(cases):
    n = int(input())
    arr = input().split()
    arr = [int(x) for x in arr]
    arrAbs = [abs(x) for x in arr]
    ans = sum(arrAbs)
    operations = 0
    flag = False
    for j in range(len(arr)):
        if arr[j] == 0:
            continue
        elif arr[j] > 0:
            if not flag:
                continue
            else:
                flag = False
        else:
            if flag:
                continue
            else:
                operations += 1
                flag = True
    
    print(f"{ans} {operations}")
