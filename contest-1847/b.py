import sys
cases = int(sys.stdin.readline()[:-1])
PRE_ANS = 2 ** 30 -1 

for fas in range(cases):
    n = int(sys.stdin.readline()[:-1])
    a = sys.stdin.readline()[:-1].split(" ")
    a = [int(x) for x in a]
    ans = PRE_ANS

    for a_ in a:
        ans = ans & a_

    if ans != 0:
        print(1)
        continue

    cnt = 0
    tmp = PRE_ANS
    for i in range(len(a)):
        tmp = tmp & a[i]
        if tmp == 0:
            cnt += 1
            tmp = PRE_ANS
    
    print(cnt)

