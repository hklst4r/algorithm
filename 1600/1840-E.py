

def solve():
    s1 = input()
    s2 = input()
    s1 = [ord(x)-ord('a') for x in s1]
    s2 = [ord(x)-ord('a') for x in s2]
    l = len(s1)
    AA = input().split(" ")
    block_t, q = int(AA[0]), int(AA[1])
    block_curr = [-1 for _ in range(l)]
    for i in range(q):
        command_ = input().split(" ")
        command =[int(x) for x in command_] 
        if command[0] == 1:
            block_curr[int(command[1] - 1)] = i + block_t - 1
        elif command[0] == 2:
            if command[1] == 1 and command[3] == 2:
                s1[command[2]-1], s2[command[4]-1] = s2[command[4]-1], s1[command[2]-1]
            elif command[1] == 2 and command[3] == 1:
                s2[command[2]-1], s1[command[4]-1] = s1[command[4]-1], s2[command[2]-1]
            elif command[1] == 1 and command[3] == 1:
                s1[command[2]-1], s1[command[4]-1] = s1[command[4]-1], s1[command[2]-1]
            elif command[1] == 2 and command[3] == 2:
                s2[command[2]-1], s2[command[4]-1] = s2[command[4]-1], s2[command[2]-1]
        else:
            flag = True
            for j in range(l):
                if s1[j] != s2[j]:
                    if block_curr[j] < i:
                        flag = False
                        print("NO")
                        break
            if flag == True:
                print("YES")

cases = int(input())
for i in range(cases):
    solve()






