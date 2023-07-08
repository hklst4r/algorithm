import sys

import time

cases = int(input())
time.sleep(1)
for _ in range(cases):
    m = [[],[],[]]
    m[0] = list(sys.stdin.readline()[:-1])
    m[1] = list(sys.stdin.readline()[:-1])
    m[2] = list(sys.stdin.readline()[:-1])

    flag = False

    for i in range(3):
        if m[i][0] == m[i][1] and m[i][1] == m[i][2] and m[i][1] != ".":
            print(m[i][0])
            flag = True
            break
        if m[0][i] == m[1][i] and m[1][i] == m[2][i] and m[0][i] != ".":
            print(m[0][i])
            flag = True
            break
    if flag:
        continue

    if m[0][0] == m[1][1] and m[1][1] == m[2][2] and m[2][2] != ".":
        print(m[0][0])
        flag = True
    if flag:
        continue

    if m[0][2] == m[1][1] and m[1][1] == m[2][0] and m[1][1] != ".":
        print( m[0][2])
        flag = True
    if flag:
        continue

    print("DRAW")



