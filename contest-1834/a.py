
cases =int(input())

for i in range(cases):
    l = int(input())
    arr = input().split(" ")
    s = sum([int(x) for x in arr])
    minusCases = (l - s) // 2
    if s >= 0 and minusCases % 2 == 0:
        ans = 0
    elif s >= 0 and minusCases % 2 == 1:
        ans = 1
    elif s < 0 and minusCases % 2 == 0:
        if s % 2 == 0:
            ans = -1 * (s) // 2 
        else:
            ans = -1 * (s) // 2 + 1
        if ans % 2 == 1:
            ans += 1
    elif s < 0 and minusCases % 2 == 1:
        if s % 2 == 0:
            ans = -1 * (s) // 2 
        else:
            ans = -1 * (s) // 2 + 1
        if ans % 2 == 0:
            ans += 1
    print(ans)
