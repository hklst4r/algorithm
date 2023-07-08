import sys
import time

cases = int(input())

for _ in range(cases):
    n, m, h = sys.stdin.readline()[:-1].split(" ")
    n = int(n)
    m = int(m)
    h = int(h)
    S = 10000000
    scores = []
    for i in range(n):
        score = 0
        totalTime = 0
        tTmp = sys.stdin.readline()[:-1].split(" ")
        tTmp = [int(x) for x in tTmp]
        tTmp.sort()
        for j in range(m):
            if totalTime + tTmp[j] <= h:
                totalTime = totalTime + tTmp[j]
                score += S - totalTime
            else:
                break
            
        scores.append(score)
    
    Jscore = scores[0]

    scores.sort(reverse=True)
    ans = scores.index(Jscore) + 1

    print(ans)