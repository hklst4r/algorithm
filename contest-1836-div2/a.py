cases = int(input())

for _ in range(cases):
    l = int(input())
    s = input().split(" ")
    robots = [int(x) for x in s]
    times = [0]* 200
    flag = False
    for i in range(l):
        times[robots[i]] += 1
    
    for j in range(1, 200):
        if times[j-1] < times[j]:
            flag = True
            print("NO")
            break
    if not flag:
        print("YES")