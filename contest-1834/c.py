cases = int(input())
# import time
for i in range(cases):
    l = int(input())
    s1 = input()
    s2 = input()
    if s1 == s2:
        print(0)
        continue
    cnt1 = 0
    cnt2 = 0
    for i in range(l):
        if s1[i] != s2[i]:
            cnt1 += 1
        if s1[i] != s2[l - i - 1]:
            cnt2 += 1
    if cnt1 == 0:
        print(0)

    if cnt1 % 2 == 0:
        cnt1 = 2 * cnt1
    else:
        cnt1 = 2 * cnt1 - 1

    if cnt2 == 0:
        cnt2 = 2
    elif cnt2 % 2 == 1:
        cnt2 = 2 * cnt2
    else:
        cnt2 = 2 * cnt2 - 1
    print(min(cnt1, cnt2))
    