cases = int(input())

import sys
import time
time.sleep(1)

for _ in range(cases):
    A = sys.stdin.readline()[:-1]
    n, m = A.split(" ")
    n = int(n)
    m = int(m)
    initState = int(sys.stdin.readline()[:-1],2)

    sideEffects = []
    canReduce = []
    days = []
    finals = []
    
    for i in range(m):
        days.append(int(sys.stdin.readline()[:-1]))
        canReduce.append(int(sys.stdin.readline()[:-1],2))
        sideEffect = int(sys.stdin.readline()[:-1],2)
        sideEffects.append(sideEffect)
        if sideEffect == 0:
            finals.append(i)
    bestDays = sum(days)*1000 + 1
    MAX_DAYS = bestDays
    if initState == 0:
        print(0)
        continue
    if len(finals) == 0:
        print(-1)
        continue
    def visit(m, idx, bestDays, initState, currState, visited, alreadyDays):
        # print("visit", idx)
        assert (currState | sideEffects[idx]) == currState
        assert visited[idx] == False
        # print(currState)
        # print(currState | sideEffects[idx])
        visited[idx] = True
        currState = currState | canReduce[idx]
        alreadyDays += days[idx]
        if alreadyDays >= bestDays:
            return bestDays
        if currState & initState == currState and bestDays > alreadyDays + days[idx]:
            return alreadyDays + days[idx]
        if currState & initState == currState:
            return bestDays
        for i in range(m):
            if (currState | sideEffects[i] == currState) and not visited[i]:
                bestDays = visit(m, i, bestDays, initState, currState, visited, alreadyDays)
                # print(bestDays)
        return bestDays
    for final in finals:
        # print("final", final)
        if bestDays <= days[final]:
            continue
        visited = {}
        for i in range(m):
            visited[i] = False
        bestDaysTmp = visit(m, final, bestDays, initState, 0, visited, 0)
        # print(bestDaysTmp)
        if bestDaysTmp < bestDays:
            bestDays = bestDaysTmp
    
    if bestDays == MAX_DAYS:
        print(-1)
    else:
        print(bestDays)


