cases = int(input())
import time


for _ in range(cases):
    a,b,c,k = input().split(" ")
    a = int(a)
    b = int(b)
    c = int(c)
    k = int(k)

    if c < max(a,b):
        print(-1)
        continue

    # case 0: c = 1
    # if c == 1:
    #     if a != 1 or b !=1:
    #         print(-1)
    #         continue
    #     else:
    #         if k > 36:
    #             print(-1)
    #             continue
    #         edge = 0
    #         aNum = 0
    #         for t in range(8):
    #             edge += (8 - t)
    #             if k < edge:
    #                 aNum = t + 1
    #                 break
    #         bNum = k - (edge - (9 - aNum))
    #         cNum = aNum + bNum
    #         print(f"{aNum} + {bNum} = {cNum}")
    #         continue
            
    if max(a,b) == c - 1 or max(a, b) == c:
            aDown = 10 ** (a-1)
            aUp = 10 ** a - 1
            bDown = 10 ** (b-1)
            bUp = 10 ** b - 1
            cDown = 10 ** (c-1)
            cUp = 10 ** c - 1
            edges, edgesPrev = 0, 0 
            flag = False
            for aNum in range(aDown, aUp + 1):
                # print(f"aNum={aNum-1}")
                bRange = [cDown - aNum, cUp - aNum]
                if bRange[0] < bDown:
                    bRange[0] = bDown
                if bRange[1] > bUp:
                    bRange[1] = bUp
                l = bRange[1] - bRange[0] + 1
                if l > 0 and edges < k and k <= edges + l:
                    flag = True
                    break
                elif l > 0:
                    edges += l
                else:
                    continue

            if flag:
                bNum = bRange[0] +k - edges - 1
                cNum = aNum + bNum
                print(f"{aNum} + {bNum} = {cNum}")
            else:
                print(-1)
                continue
                

    else:
        print(-1)
        continue





    # # case 1: max(a, b) = c
    # if max(a, b) == c:
    #     if b == c:
    #         # total = 9 * 10**(b-1) * (10**(b-1) * 8 - 1) - 4 * 10**(b-1) * (10**(b-1) - 1)
    #         # if k > total:
    #         #     print(-1)
    #         #     continue
    #         edges, edgesPrev = 0, 0 
    #         down = 10**(a-1)
    #         up = 10**a - 1 - 10**(a-1)
    #         up_1 = 10 ** b
    #         flag = False
    #         for aNum in range(down, up):
    #             if edges > k:
    #                 flag = True
    #                 break
    #             edgesPrev = edge
    #             edges += up_1 - aNum - down
    #         if flag == False:
    #             print(-1)
    #             continue
    #         bNum = k - edgesPrev
    #         print(f"{aNum} + {bNum} = {cNum}")
    #         continue

    #     elif a == c:
    #         edges, edgesPrev = 0, 0 
    #         down = 10**(a-1)
    #         up = 10**a - 1 - 10**(a-1)
    #         up_1 = 10 ** b
    #         flag = False
    #         for aNum in range(down, up):
    #             if edges > k:
    #                 flag = True
    #                 break
    #             edgesPrev = edge
    #             edges += up_1 - aNum - down
    #         if flag == False:
    #             print(-1)
    #             continue
    #         bNum = k - edgesPrev
    #         print(f"{aNum} + {bNum} = {cNum}")
    #         continue
    
    # elif max(a, b) == c:
    #     edges, edgesPrev = 0, 0 
    #     down = 10**(a-1)
    #     up = 10**a - 1
    #     up_1 = 10 ** b
    #     for aNum in range(down, up):
    #         if edges > k:
    #             break
    #         edgesPrev = edge
    #         edges += up_1 - aNum - down
    #     bNum = k - edgesPrev
    #     print(f"{aNum} + {bNum} = {cNum}")
    #     continue
            


    # # case 2: max(a,b) = c - 1

    # # others
    # else:
    #     print(-1)
    #     continue
    # if c < a or  c < b:
    #     print(-1)
    #     continue
    # if c >= a + 2 and c >= b + 2:
    #     print(-1)
    #     continue





    # # case 2: max(a,b) = c - 1
