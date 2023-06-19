
cases = int(input())
import time
time.sleep(1)
for i in range(cases):
    a, b = input().split(" ")
    a = list(str(a))
    b = list(str(b))
    l = len(b)
    ans = 0
    strict = True
    if l > len(a):
        a = [0] * (l - len(a)) + a
    if a == b:
        print(0)
        continue
    flag = False


    for i in range(l):
        
        if a[i] == 0 and flag == False:
            if strict:
                ans += abs(int(b[i]) - int(a[i]))
            else:
                ans += 9
            strict = False
            continue
        flag = True
        if a[i] == b[i] and strict:
            continue
        if a[i] == b[i] and not strict:
            strict = False
            ans += (l - i) * 9
            break
        if a[i] != b[i]:
            if not strict:
                ans += (l - i) * 9
            else:
                ans += (l - i - 1) * 9
                ans += abs(int(b[i]) - int(a[i]))
            break
    print(ans)

