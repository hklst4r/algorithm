cases = int(input())

import time
time.sleep(1)

for k in range(cases):
    q = int(input())
    s = input().split(" ")
    a = [int(x) for x in s]
    beautifulA = []
    ans = []
    curr = -1
    flag = False
    firstA = a[0]
    for j in range(q):
        if a[j] >= curr and flag == False:
            ans.append("1")
            beautifulA.append(a[j])
        elif a[j] < curr and flag == False:
            if a[j] <= firstA:
                flag = True
                beautifulA.append(a[j])
                ans.append("1")
            else:
                ans.append("0")
        elif flag == True:
            if a[j] <= firstA and a[j] >= curr:
                beautifulA.append(a[j])
                ans.append("1")
            else:
                ans.append("0")

        curr = beautifulA[-1]
    print(''.join(ans))

